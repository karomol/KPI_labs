from locust import HttpUser, task, between

class User(HttpUser):

    host = 'https://reqres.in/api'
    time = between(1, 5)


    @task(1)
    def getUser(self):
        self.client.get("/users/6")

    @task(2)
    def addUser(self):
        self.client.post("/users", json={
            "email": "eve.holt@reqres.in",
            "password": "cityslicka"
        })

    @task(1)
    def updateUser(self):
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
    def deleteUser(self):
        self.client.delete("/users/6")
