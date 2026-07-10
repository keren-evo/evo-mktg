# Link Homecare CRM Status Mapping

## 1. Lead and Patient Status Mapping


| Status Group       | Current Status | New Status           | Rule / Notes                                                                                        |
| ------------------ | -------------- | -------------------- | --------------------------------------------------------------------------------------------------- |
| **Lead Status**    | New            | Lead                 |                                                                                                     |
| **Lead Status**    | In Progress    | Qualifying           |                                                                                                     |
| **Lead Status**    | Dropped Off    | Lead Dropped Off     |                                                                                                     |
| **Lead Status**    | Converted      |                      |                                                                                                     |
| **Patient Status** | Pre Intake     |                      |                                                                                                     |
| **Patient Status** | In Progress    | Referral In Progress | Set if a non-short-term intake is opened. Push back to **Qualifying** if there is no active intake. |
| **Patient Status** | Authorized     | Active               |                                                                                                     |
| **Patient Status** | Dropped Off    | Dropped Off          |                                                                                                     |
| **Patient Status** | Closed         | Discharged           |                                                                                                     |


---



## 2. Line-of-Business Status Mapping


| Current LOB Status | Condition / Rule                                                                                                                           | New LOB Status |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ | -------------- |
| Interested         |                                                                                                                                            | Interested     |
| Not Interested     |                                                                                                                                            | Not Interested |
| New Intake         | Not short-term                                                                                                                             | New Intake     |
| In Progress        |                                                                                                                                            | In Progress    |
| Active             |                                                                                                                                            | Active         |
| Expiring           |                                                                                                                                            | Expiring       |
| Expired            |                                                                                                                                            | Expired        |
| Future Start       |                                                                                                                                            | Future Start   |
| Dropped            |                                                                                                                                            | Dropped        |
| Discharged         |                                                                                                                                            | Discharged     |
| Intake Dropped     | Remove this status. When an intake is dropped, ask: **Continue pursuing the patient?** Yes → Interested; No → Drop Line.                   |                |
| Voided Auth        | Not short-term                                                                                                                             | Voided Auth    |
| Not Authorized     | Short-term only                                                                                                                            | Skilled Only   |
| Non-Admit          | Short-term only                                                                                                                            | Non-Admit      |
| Accepted           | Short-term only                                                                                                                            | Accepted       |
| Missing Info       |                                                                                                                                            | Missing Info   |
| Non-Admit Closed   | Short-term only. Remove this status. When the intake is dropped, ask: **Continue pursuing the patient?** Yes → Interested; No → Drop Line. |                |


---



## 3. Current LOB Discharge Reasons


| Current LOB Discharge Reason |
| ---------------------------- |
| Switched line of business    |
| Account drop / discharge     |


---



## 4. Decision Logic



### Intake Dropped

When an intake is dropped:

```text
Continue pursuing the patient?
├── Yes → LOB Status = Interested
└── No  → Drop Line
```

