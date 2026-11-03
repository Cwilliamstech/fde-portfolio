# Job ID and current state get saved
# gets saved after each transition 
# jobs get loaded once, when the script starts. 

import json
allowed_transitions = {"draft" : ["pending_approval"], "pending_approval" : ["approved", "rejected"], "approved" : ["sent"], "rejected" : ["draft"], "sent" : []}
jobs = {"job_1" : "draft", "job_2" : "pending_approval"}
human_only = ["approved", "rejected"]
def move_job(current_state, next_state, actor):
    allowed = allowed_transitions.get(current_state, [])
    if next_state in human_only and actor != "human":
        return False
    if next_state in allowed:
        return True
    else:
        return False

def save_jobs(jobs):
    with open("jobs.json", "w") as f:
        json.dump(jobs, f)
save_jobs(jobs)

        

print(move_job("pending_approval", "rejected", "ai"))
print(move_job("pending_approval", "approved", "human"))