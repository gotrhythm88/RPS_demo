from fastapi import FastAPI
import random

app = FastAPI()

@app.get("/")
def read_root():
  return {"Hello": "RPS player"}


@app.get("/rps_score/playermove/{player_choice}")
def score_rps(player_choice: str):
  api_choice = random.choice(["rock","paper","scissors"])
  result = ""
  
  if api_choice == player_choice:
    result = "It's a tie!"
  elif api_choice == "rock" and player_choice == "paper":
    result = "You Win!!"
  ### 5 more cases
  else:
    result = "Unable to determine winner"

    '''
    {	“status”: “success/failure”, 
	“apimove”: “rock/paper/scissors”, 
	“result”: “You win!/The API defeated you/It’s a tie”   }
    '''

  output = {}
  if result == "Unable to determine winner":
    output["status"] = "failure"
  else:
    output["status"] = "success"
  
  output["apimove"] = api_choice
  output["result"] = result

  return output
