def review_request(request, decision):

    if decision.lower() == "approve":
        request["status"] = "Approved"
        print("Request Approved")
        return "Approved"

    request["status"] = "Rejected"
    request["approval_reason"] = "Manager rejected"
    print("Request Rejected")
    return "Rejected"