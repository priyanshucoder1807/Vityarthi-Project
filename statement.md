### Objective

Build an automated medical dispatch and scheduling system for university health services that replaces manual logbooks with real-time slot verification and structured patient intake.

---

### Core Requirements

1. **Patient Verification & Intake**
* Capture student details: *Full Name*, *Registration Number*, *Age* , and *Phone Number* .
* Utilize crash-proof validation loops to handle non-numeric or malformed entries cleanly.


2. **Specialty & Tariff Directory**
* Present an index of clinical departments (General Practice, Cardiology, Orthopedics, Pediatrics, Dermatology) mapped directly to their consultation costs.


3. **Temporal Constraint Checking**
* Compare user-selected calendar dates against current system time to reject historical bookings.
*Expose standardized daily operating windows for student selection.


4. **Slot Collision Defense**
* Enforce scheduling integrity by preventing overlapping reservations for any given (Department, Date, Time) combination.


5. **Tracking Hash & Master Roster**
* Issue a unique reference identifier  for every completed reservation.
* Render an itemized confirmation receipt and record the entry in an active master ledger for clinic administration.



---

### Key Specifications

* **Architecture:** Object-Oriented Design in Python 3 (dataclasses and controller classes)
* **Dependencies:** Python Standard Library only (datetime, dataclasses, typing)
* **Interface:** Interactive terminal menu loop