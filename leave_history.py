leave_history = []

def show_history(request):

    leave_history.append(request)

    print("Leave History")
    for item in leave_history:
        print(item)