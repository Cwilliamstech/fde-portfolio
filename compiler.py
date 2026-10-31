from mcp.server.fastmcp import FastMCP

mcp = FastMCP("job-compiler")

@mcp.tool()
def compile_jobs():
    """Returns a list of jobs ranked by due date. Read only. Never alters data"""
    with open("jobs_report.txt") as f:
        report_text = f.read()
    jobs = []
    parts = report_text.split("\n")
    for part in parts:
        if part == "":
            continue
        new_part = part.strip().split("|")
        if new_part[0] == "JOB" or new_part[-1] == "ON HOLD":
            continue
        else:
            task = {"job" : new_part[0], "address" : new_part[1], "task" : new_part[2], "trade" : new_part[3], "due" : new_part[4], "status" : new_part[5]}
            jobs.append(task)
    return sorted(jobs, key=lambda t: t["due"])


@mcp.tool()
def draft_schedule():
    """returns a list of jobs with crew members scheduled based on skills and availability. Read only. Never alters any data. OUTPUT IS A DRAFT THAT NEEDS HUMAN APPROVAL"""
    with open("crew.txt") as f:
        crew_text = f.read()
    jobs = compile_jobs()
    employees= crew_text.split("\n")
    crew = []
    assigned = []
    for employee in employees:
        employee = employee.strip().split("|")
        if employee[0] == "NAME" or employee[0] == "":
            continue
        else:
            person = {"name" : employee[0], "trades" : employee[1].split(","), "availability" : employee[2].split(",")}
            crew.append(person)
    for job in jobs:
        for person in crew:
            if job["trade"] in person["trades"] and job["due"] in person["availability"]:
                complete = {"task" : job["task"], "trade" : job["trade"], "assigned" : person["name"]}
                assigned.append(complete)
                person["availability"].remove(job["due"])
                break
        else:
            complete = {"task" : job["task"], "trade" : job["trade"], "assigned" : "no one available"}
            assigned.append(complete)
    return assigned

                

     

                

                
     

                           
   
                

            
            
   

   
    




#create crew matrix
#check crew capabilities agains job requirements 
#check matching capabilities crew members availability to due date
#return list of crew whos capabilities and availability match 
                


if __name__ == "__main__":
    mcp.run()






    