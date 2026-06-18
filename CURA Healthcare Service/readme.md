# CURA Healthcare Appointment Automation 🧠

This project automates the process of booking an appointment on the **CURA Healthcare Service** demo website using **Selenium WebDriver** in **Microsoft Edge (InPrivate)** mode.

---

## ▶️ How to Run

```

### Run with PyTest and generate report

```bash
pytest -s main.py --alluredir=reports
allure serve reports
```

---

## 🧰 What the Script Does

1. Opens `https://katalon-demo-cura.herokuapp.com/`
2. Clicks **Make Appointment**
3. Logs in using:

   * Username: `John Doe`
   * Password: `ThisIsNotAPassword`
4. Fills appointment details:
   * Facility: *Hongkong CURA Healthcare Center*
   * Program: *Medicaid*
   * Visit Date: *30th*
   * Comment: *“This is an automated appointment request.”*
5. Books the appointment
6. Prints:

   ```
   Appointment successfully booked! Browser will close in 10 seconds.
   ```

<img width="1919" height="995" alt="Screenshot 2026-01-20 002156" src="https://github.com/user-attachments/assets/53af64f3-c092-47cf-8bea-b9a2ac426165" />

<img width="1920" height="1050" alt="Screenshot 2026-01-20 002301" src="https://github.com/user-attachments/assets/086c2df9-f8a2-435e-9f78-4c531b13b0b2" />

<img width="1920" height="1050" alt="Screenshot 2026-01-20 002326" src="https://github.com/user-attachments/assets/5a994731-bb63-43f3-9993-9936cad41ecb" />

<img width="1919" height="953" alt="Screenshot 2026-01-20 002211" src="https://github.com/user-attachments/assets/af18b0de-e8e6-4d13-afb5-e5c04d3e3493" />




   
