allowed_transitions = {"draft" : ["pending_approval"], "pending_approval" : ["approved", "rejected"], "approved" : ["sent"], "rejected" : ["draft"], "sent" : []}

def move_job(current_state, next_state, actor):
    human_only = ["approved", "rejected"]
    allowed = allowed_transitions.get(current_state, [])
    if next_state in human_only and actor != "human":
        return False
    if next_state in allowed:
        return True
    else:
        return False

print(move_job("pending_approval", "rejected", "ai"))
print(move_job("pending_approval", "approved", "human"))