alx_travel_app_0x00

This is a Django-based travel application for the ALX Backend Specialization.  
In this milestone, we focus on **database modeling**, **serialization**, and **data seeding**.

---

## 📦 Project Structure

alx_travel_app_0x00/
├── alx_travel_app/
│ ├── listings/
│ │ ├── models.py
│ │ ├── serializers.py
│ │ └── management/
│ │ └── commands/
│ │ └── seed.py
│ ├── manage.py
│ └── ...
└── README.md

yaml
Copier
Modifier

---

## 🧠 Models

### 📌 Listing

Represents a travel listing.

| Field            | Type              | Description                   |
|------------------|-------------------|-------------------------------|
| title            | CharField         | Title of the listing          |
| description      | TextField         | Full description              |
| price_per_night  | DecimalField      | Price per night               |
| location         | CharField         | Location of the listing       |
| owner            | ForeignKey (User) | Owner of the listing          |
| created_at       | DateTimeField     | Timestamp of creation         |

---

### 📌 Booking

Represents a booking for a listing.

| Field       | Type              | Description               |
|-------------|-------------------|---------------------------|
| listing     | ForeignKey        | Related listing           |
| user        | ForeignKey (User) | User who made the booking |
| start_date  | DateField         | Start date of the booking |
| end_date    | DateField         | End date of the booking   |
| created_at  | DateTimeField     | Timestamp of creation     |

---

### 📌 Review

Represents a review of a listing.

| Field       | Type              | Description               |
|-------------|-------------------|---------------------------|
| listing     | ForeignKey        | Reviewed listing          |
| user        | ForeignKey (User) | Reviewer                  |
| rating      | IntegerField      | Rating (1-5)              |
| comment     | TextField         | Review comment            |
| created_at  | DateTimeField     | Timestamp of creation     |

---

## 🔁 Serializers

Located in `listings/serializers.py`, the serializers allow model instances to be converted to JSON for API interaction.

- `ListingSerializer`
- `BookingSerializer`

---

## 🌱 Data Seeding

### ✨ What it does:
Seeds the database with sample travel listings.

### 📂 File Location:
listings/management/commands/seed.py

perl
Copier
Modifier

### ▶️ Run Seeder

From the root of the project (same folder as `manage.py`):

```bash
python manage.py seed
You should see output like:

nginx
Copier
Modifier
Creating sample listings...
5 sample listings created!
⚙️ Setup Instructions
1. Clone the repo
bash
Copier
Modifier
git clone <repo-url>
cd alx_travel_app_0x00/alx_travel_app
2. Create and activate a virtual environment
bash
Copier
Modifier
python3 -m venv venv
source venv/bin/activate
3. Install dependencies
bash
Copier
Modifier
pip install -r requirements.txt
4. Run migrations
bash
Copier
Modifier
python manage.py makemigrations
python manage.py migrate
5. Create a superuser (optional)
bash
Copier
Modifier
python manage.py createsuperuser
6. Run the development server
bash
Copier
Modifier
python manage.py runserver
