# Django CSV Processing with Celery & Redis  

## 🚀 Project Overview  
This project allows users to upload CSV files, process numerical data asynchronously using **Celery & Redis**, and dynamically display the results with a search functionality.  

## 📌 Features  
- Upload CSV files with numerical data  
- Asynchronous processing using Celery  
- Calculate **Sum, Average, and Count** for numeric columns  
- Additional insights:
  - **Total Revenue** (Sum of Sales)  
  - **Best-Selling Product** (Highest Sum of Quantity)  
  - **Most Profitable Product** (Highest Sum of Profit)  
  - **Product with Maximum Discount**  
- Search functionality for filtering results dynamically  

---

## 🛠️ Technologies Used  
- **Django** (Backend)  
- **Celery & Redis** (Asynchronous Task Processing)  
- **Pandas** (Data Processing)  
- **Bootstrap 5 & JavaScript** (Frontend)  

---

## 🏗️ Setup Instructions  

### 1️⃣ **Clone the Repository**  
```sh
git clone https://github.com/Sanjay-7222/csv_processor.git
cd csv_processor

To run this project, you need to start Django, run Redis, and launch the Celery worker.

python manage.py runserver
redis-server
celery -A myproject worker --loglevel=info --pool=solo


📬 Contact
Feel free to reach out if you have any questions!
📧 Email: sanjay8015803208@gmail.com
🔗 LinkedIn: http://linkedin.com/in/sanjay-p-b1a639318
📂 GitHub: https://github.com/Sanjay-7222