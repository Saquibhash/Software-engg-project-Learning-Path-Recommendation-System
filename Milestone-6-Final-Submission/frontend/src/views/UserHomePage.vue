<template>
      <UserNavComponent>
        <div style="padding-bottom: 100px;"></div>
        <div class="container">
          <div class="row justify-content-center mb-4">
              <h1 class="text-center" style="font-weight: 600; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; color: #2c3e50;">Welcome, {{ userData.name }}!!!</h1>
          </div>
          <div style="padding-bottom: 100px;"></div>
          <div class="row justify-content-center">
              <div class="col-md-6">
                  <div class="card border-0 shadow">
                      <div class="card-body">
                        <ul class="list-group list-group-flush">
                          <h5 class="card-title mb-4">Student Details</h5>
                          <li class="list-group-item"><strong>Name:</strong> {{ userData.name }}</li>
                          <li class="list-group-item"><strong>Level:</strong> {{ userData.level }}</li>
                          <li class="list-group-item"><strong>Email:</strong> {{ userData.email }}</li>
                          <li class="list-group-item"><strong>CGPA:</strong> {{ userData.cgpa }}</li>
                        </ul>
                      </div>
                  </div>
              </div>
          </div>
      </div>


</UserNavComponent>

  </template>
  
  <script>
  import { mapGetters } from "vuex";

  export default {
    name: "UserHomePage",
    data() {
      return {
      //get the profile details and disply it.
      };
    },
    computed: {
        ...mapGetters(["getUserData"]),
        userData() {
            return this.getUserData[0];
        },
    },
  
  };
  </script>
  <style>
</style>
  