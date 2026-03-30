def create_leave_request(start_date, end_date, reason, leave_type):

    request = {
        "start_date": start_date,
        "end_date": end_date,
        "reason": reason,
        "type": leave_type,
        "status": "Pending"
    }

    print("Leave Request Submitted")

    request["employee"] = "employee"
    return request