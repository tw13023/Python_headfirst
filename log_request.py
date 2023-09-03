def log_request(req:'flask_request',res: str) -> None:
    with open('vsearch.log', 'w') as log:
        print(req,res, file=log)
        
    