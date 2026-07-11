# Mixpanel implementation specification

Generated: 2026-07-11  
Mode: Quick Start  
Audience: developer handoff

## Executive summary

This specification sets up the first useful Mixpanel foundation for a public lead form or marketing site.

The chosen Value Moment is `lead_created`. That is the first trustworthy signal that marketing traffic turned into an actual CRM or database record. For this kind of flow, the right first build is not a full product funnel. It is clean lead creation tracking with strong attribution and consent-safe browser capture.

This spec uses a hybrid pattern:

- Browser SDK for consented client-side capture, Autocapture, Session Replay, and passing the anonymous Mixpanel ID with the form submission.
- Existing server or warehouse pipeline for the authoritative `lead_created` event after the lead is actually created.

Estimated implementation time: 2 to 4 hours

## 1. Technical foundation

### Platform and tracking method

- Platform: web app / JavaScript
- Entry flow: public lead form or marketing site
- Tracking method: hybrid
  - client-side Mixpanel browser SDK for session-level capture
  - server-side or warehouse pipeline for authoritative business events
- Existing pipeline note: do not fire `lead_created` only from the browser. It should come from the system that actually creates the lead record.

### Why this approach

`lead_created` is a business event, not just a click or form interaction. If it fires only in the browser, you will lose events to blockers, retries, duplicate submits, and validation failures. The browser is still useful for pre-submit behavior, Autocapture, and Session Replay.

### SDK and installation

Browser SDK:

```bash
npm install mixpanel-browser
```

### Token storage

Do not hardcode the Mixpanel token in source files.

Use:

- `NEXT_PUBLIC_MIXPANEL_TOKEN` for the browser SDK
- `MIXPANEL_PROJECT_TOKEN` for the server or pipeline event sender

Set both env vars to the Mixpanel project token that was provided separately.

### Consent and privacy

Regulated-region status is unknown, so use the conservative default:

- initialize Mixpanel with tracking opted out by default
- only opt in after explicit consent
- do not put email, phone, full name, or free-text notes into event properties

### Web features

- Autocapture: enabled
- Session Replay: enabled at `10%`

Important:

- Do not set `track_pageview: true` when `autocapture: true` is enabled.
- Do not add manual `page_viewed` tracking unless there is a very specific reason.

## 2. Business context

### Value Moment

`lead_created`

Meaning: a real lead record was successfully created in the CRM or the system of record.

Why it matters:

- It is the first event that should be trusted for marketing-to-CRM conversion.
- It creates a clean denominator for source, campaign, and referral reporting.
- It lets the team measure attribution hygiene without pretending downstream lifecycle states are already clean.

### First two events

Because this is a public lead flow rather than an authenticated product signup, this spec substitutes the usual Quick Start `sign_up_completed` event with `lead_form_submitted`.

Priority order:

1. `lead_created`
2. `lead_form_submitted`

## 3. Tracking plan

### Event 1: `lead_form_submitted`

- Trigger: after the form submission succeeds and the server returns success
- Do not fire on button click
- Fire from: browser

Required properties:

- `form_name` string  
  Example: `"main_intake_form"`
- `service_line` string  
  Example: `"home_health_aide"`
- `market` string  
  Example: `"ny"`

Optional properties:

- `referral_source` string
- `landing_path` string
- `cta_location` string

Notes:

- UTM parameters are auto-collected by the browser SDK, so do not manually duplicate `utm_source`, `utm_medium`, `utm_campaign`, `utm_content`, or `utm_term`.
- Omit optional properties when blank.

### Event 2: `lead_created`

- Trigger: after the lead record is successfully written to the CRM, database, or authoritative pipeline
- Fire from: server or existing warehouse/custom pipeline
- This is the Value Moment event

Required properties:

- `lead_id` string  
  Use the stable CRM or database lead ID
- `lead_source` string  
  Example: `"referral"`, `"marketer"`, `"facility"`, `"phone"`
- `service_line` string  
  Example: `"home_health_aide"`
- `submission_channel` string  
  Example: `"web_form"`

Optional properties:

- `campaign_name` string
- `referral_source` string
- `market` string
- `owner_id` string

Identity requirement:

- Include the anonymous Mixpanel browser ID from the form submission as `$device_id`
- Include the stable lead ID as `$user_id`

That lets Mixpanel stitch anonymous browser behavior to the created lead.

## 4. Implementation guide

### Step 1: initialize Mixpanel in the browser

Where to add this:

- app entry point
- root layout
- shared analytics bootstrap file

Recommended file name:

- `src/lib/mixpanel.js`

```javascript
import mixpanel from "mixpanel-browser";

let initialized = false;

export function initMixpanel() {
  if (initialized) return;

  mixpanel.init(process.env.NEXT_PUBLIC_MIXPANEL_TOKEN, {
    debug: process.env.NODE_ENV !== "production",
    persistence: "localStorage",
    autocapture: true,
    record_sessions_percent: 10,
    opt_out_tracking_by_default: true,
  });

  mixpanel.register({
    platform: "web",
  });

  initialized = true;
}

export function grantAnalyticsConsent() {
  mixpanel.opt_in_tracking();
}

export function denyAnalyticsConsent() {
  mixpanel.opt_out_tracking();
}

export function canTrack() {
  return mixpanel.has_opted_in_tracking();
}

export function getAnonymousMixpanelId() {
  return mixpanel.get_distinct_id();
}
```

Implementation notes:

- Call `initMixpanel()` once at app startup.
- Call `grantAnalyticsConsent()` only after explicit user consent.
- Keep `denyAnalyticsConsent()` wired to consent refusal or withdrawal.

### Step 2: pass the anonymous Mixpanel ID with the lead form

Where to add this:

- shared form component
- lead capture page script

```javascript
import { getAnonymousMixpanelId } from "./mixpanel";

export function attachMixpanelIdToLeadForm(formElement) {
  let input = formElement.querySelector('input[name="mixpanel_device_id"]');

  if (!input) {
    input = document.createElement("input");
    input.type = "hidden";
    input.name = "mixpanel_device_id";
    formElement.appendChild(input);
  }

  input.value = getAnonymousMixpanelId();
}
```

Call this after the form renders and before submission.

### Step 3: track `lead_form_submitted` from the browser

Where to add this:

- in the form success handler
- after the server confirms success

```javascript
import mixpanel from "mixpanel-browser";
import { canTrack } from "./mixpanel";

export function trackLeadFormSubmitted({
  formName,
  serviceLine,
  market,
  referralSource,
  ctaLocation,
}) {
  if (!canTrack()) return;

  const props = {
    form_name: formName,
    service_line: serviceLine,
    market,
    landing_path: window.location.pathname,
  };

  if (referralSource) props.referral_source = referralSource;
  if (ctaLocation) props.cta_location = ctaLocation;

  mixpanel.track("lead_form_submitted", props);
}
```

Do not:

- fire this on button click
- send raw email, phone, or name in properties
- duplicate page view tracking when Autocapture is already on

### Step 4: send `lead_created` from the authoritative backend or pipeline

Where to add this:

- right after the lead row or CRM record is created
- or inside the existing event pipeline that receives confirmed lead creation

Use the Mixpanel HTTP API if the backend language is unknown or mixed:

```bash
curl --request POST \
  --url https://api.mixpanel.com/track \
  --header 'Content-Type: application/json' \
  --data '[{
    "event": "lead_created",
    "properties": {
      "token": "'"$MIXPANEL_PROJECT_TOKEN"'",
      "$device_id": "mixpanel-anonymous-id-from-form",
      "$user_id": "crm-lead-id-12345",
      "time": 1783785600,
      "$insert_id": "crm-lead-id-12345:lead_created",
      "lead_id": "crm-lead-id-12345",
      "lead_source": "referral",
      "service_line": "home_health_aide",
      "submission_channel": "web_form",
      "market": "ny"
    }
  }]'
```

Implementation rules:

- Always set `$insert_id` to a stable unique value so retries do not create duplicates.
- Use the CRM or database lead ID as `$user_id`.
- Use the hidden `mixpanel_device_id` from the browser as `$device_id`.
- If `campaign_name` or `referral_source` is blank, omit it.
- If privacy policy allows and consent is present, forward client IP for geolocation. If not, omit it.

### Step 5: optional lead profile

Use this only if the privacy policy and consent model allow it.

Do not send personal data as event properties. If needed, store it only in the user profile layer.

A safe starter profile can stay non-PII:

```bash
curl --request POST \
  --url https://api.mixpanel.com/engage \
  --header 'Content-Type: application/json' \
  --data '[{
    "$token": "'"$MIXPANEL_PROJECT_TOKEN"'",
    "$distinct_id": "crm-lead-id-12345",
    "$ip": "0",
    "$set": {
      "lead_source": "referral",
      "service_line": "home_health_aide",
      "market": "ny",
      "first_touch_channel": "web_form"
    }
  }]'
```

If legal and policy review approve it, profile fields like `$email` can be added later. Do not start there.

## 5. Verification and testing

### Pre-deploy checklist

- Browser SDK initializes once
- Consent gate blocks tracking before opt-in
- Autocapture is enabled
- `track_pageview` is not enabled
- Lead form includes `mixpanel_device_id`
- `lead_form_submitted` fires only after success
- `lead_created` fires only after the authoritative lead write succeeds
- `$insert_id` is unique and stable on retries

### Live View test plan

1. Open Mixpanel Live View in the development project.
2. Visit the lead form page in a clean browser session.
3. Accept analytics consent.
4. Submit a test lead successfully.

Expected result 1:

- Event name: `lead_form_submitted`
- Appears within about 60 seconds
- Properties include `form_name`, `service_line`, `market`, and `landing_path`
- UTM properties should be present if they were on the landing URL

Expected result 2:

- Event name: `lead_created`
- Appears within about 60 seconds of the backend or pipeline write
- Contains `lead_id`, `lead_source`, `service_line`, `submission_channel`
- Uses the same anonymous browser session through `$device_id`, then merges to the stable lead ID via `$user_id`

### Session Replay note

Replay is configured at `10%`, so not every session will be recorded.

If the team wants guaranteed replay during testing, temporarily raise `record_sessions_percent` to `100` in development only.

## 6. Common failure modes

### Problem: no browser events show up

Check:

- `grantAnalyticsConsent()` was actually called
- `NEXT_PUBLIC_MIXPANEL_TOKEN` is defined
- `initMixpanel()` runs before the form logic
- browser network requests to Mixpanel are not blocked

### Problem: duplicate page views or noisy event volume

Check:

- `track_pageview` is not enabled anywhere
- no manual `page_viewed` call was added on top of Autocapture
- Mixpanel is initialized only once

### Problem: `lead_created` appears but does not stitch to the browser session

Check:

- the browser sent `mixpanel_device_id`
- the backend passed that value through as `$device_id`
- the backend used a stable CRM or DB lead ID as `$user_id`

### Problem: duplicate `lead_created` events

Check:

- retries use the same `$insert_id`
- the event is fired from exactly one authoritative place
- both the browser and backend are not sending the same business event

### Problem: campaign and source data are still blank

Check:

- landing URLs actually include UTM parameters
- the CRM write path persists source and campaign fields
- the pipeline maps those fields into `lead_source`, `campaign_name`, and `referral_source`

## 7. Naming and data rules

- Use `snake_case` for event names, property names, and enum-like values
- One event, one meaning
- Omit empty properties instead of sending blank strings or nulls
- Do not use `$` or `mp_` prefixes for custom properties
- Do not send raw PII in event properties

Recommended starter enum values:

- `submission_channel`: `"web_form"`, `"phone"`, `"marketer"`, `"facility"`
- `market`: `"ny"`, `"nj"`, `"pa"` or your actual market list
- `lead_source`: reuse the business-approved CRM source names exactly once they are settled

## 8. Recommended next events after this Quick Start

Once the first two events are flowing cleanly, add these next:

1. `lead_attributed`
2. `follow_up_due`
3. `follow_up_completed`
4. `pre_active_exited`
5. `status_conflict_detected`

That sequence matches the actual reporting pain in this workspace better than jumping straight to deeper lifecycle metrics.

## 9. Resources

- Mixpanel JavaScript SDK: https://docs.mixpanel.com/docs/tracking-methods/sdks/javascript
- Mixpanel HTTP API: https://developer.mixpanel.com/reference/track-event
- Mixpanel identity management: https://docs.mixpanel.com/docs/tracking-methods/id-management/identifying-users
- Mixpanel default properties: https://docs.mixpanel.com/docs/data-structure/property-reference/default-properties
- Mixpanel Lexicon: https://docs.mixpanel.com/docs/data-governance/lexicon

## Bottom line

The key decision in this spec is simple.

Use the browser SDK to capture consented session context. Use the server or warehouse pipeline to emit the one event that actually matters first, `lead_created`, after the CRM record exists. That gives you attribution you can trust without pretending the rest of the lifecycle is already clean.
