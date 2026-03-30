from auth import login
from leave_request import create_leave_request
from manager_review import review_request
from leave_history import show_history
from notifications import notify

print("Employee Leave Management System")

user = login("employee", "1234")

if user:
    request = create_leave_request("2026-04-01", "2026-04-03", "Medical Leave", "Sick")
    status = review_request(request, "approve")
    notify(status)
    show_history(request)

print("UI Improved")