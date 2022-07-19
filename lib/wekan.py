import urequests as requests
import json


class Wekan:
    def __init__(self, url, username, password):
        self.username = username
        self.password = password
        self.url = url
        print("[WEKAN] Login...")
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': '*/*'
        }
        body = requests.post(url + "/users/login" , data="username="+username+"&password="+password, headers=headers)
        print("[WEKAN] Response")
        print(body.text)
        json = body.json()
        try:
            print("[WEKAN] Login success")
            self.token = json["token"]
            self.id = json["id"]
        except:
            print("[WEKAN] Login Failed")
        self.headers = {
                            "Authorization": "Bearer " + self.token,
                            "Content-Type": "application/json"
                        }
        self.status = True

    def get_boards(self):
        if self.status:
            print("[WEKAN] Get boards")
            body = requests.get(self.url + "/api/users/" + self.id + "/boards", headers=self.headers)
            print("[WEKAN] Response")
            print(body.text)
            return body
        else:
            print("[WEKAN] : Not connected")
            return False

    def get_lists(self, board):
        if self.status:
            print("[WEKAN] Get Lists from " + board)
            body = requests.get(self.url + "/api/boards/" + board + "/lists", headers=self.headers)
            print("[WEKAN] Response")
            print(body.text)
            return body
        else:
            print("[WEKAN] : Not connected")

    def get_cards(self, board, todolist):
        if self.status:
            print("[WEKAN] Get Cards from " + todolist)
            body = requests.get(self.url + "/api/boards/" + board + "/lists/" + todolist + "/cards", headers=self.headers)
            print("[WEKAN] Response")
            print(body.text)
            return body
        else:
            print("[WEKAN] : Not connected")
            return False

    def get_card_info(self, board, todolist, card):
        if self.status:
            print("[WEKAN] Get Card info " + card)
            body = requests.get(self.url + "/api/boards/" + board + "/lists/" + todolist + "/cards/" + card, headers=self.headers)
            print("[WEKAN] Response")
            print(body.text)
            return body
        else:
            print("[WEKAN] : Not connected")
            return False
    
    def get_last_card(self, board, todolist):
        if self.status:
            body = self.get_cards(board, todolist)
            return body.json()[0]["_id"]
        
    def add_time(self, board, todolist, card):
        if self.status:
            body = self.get_card_info(board,todolist,card)
            spentTime = body.json()["spentTime"]
            if spentTime == None:
                spentTime = 1
            else:
                spentTime = spentTime + 1
            print("[WEKAN] Add " + str(spentTime) + " to card " + card)
            data = {
                "board": board,
                "list": todolist,
                "card": card,
                "spentTime":spentTime
            }
            body = requests.put(self.url + "/api/boards/" + board + "/lists/" + todolist + "/cards/" + card, data=json.dumps(data), headers=self.headers)
            print(body.text)
            return body
        else:
            print("[WEKAN] : Not connected")
            return False

