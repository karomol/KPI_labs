from locust import HttpUser, task, between

class User(HttpUser):

    host = 'https://reqres.in/api'
    time = between(1, 5)


    @task(1)
    def GetUser(self):
        self.client.get("/users/6")

    @task(2)
    def AddUser(self):
        self.client.post("/users", json={
            "email": "eve.holt@reqres.in",
            "password": "cityslicka"
        })

    @task(1)
    def UpdateUser(self):
        self.client.patch("/users", json={
            "email": "eve.holt@reqres.in",
            "password": "cityslicka45343"
        })

    @task(3)
    def RegisterUser(self):
        self.client.post("/users", json={
            "email": "eve.holt@reqres.in",
            "password": "pistol"
        })

    @task(3)
    def LoginUser(self):
        self.client.post("/users", json={
            "email": "eve.holt@reqres.in",
            "password": "pistol"
        })

    @task(1)
    def DeleteUser(self):
        self.client.delete("/users/6")
