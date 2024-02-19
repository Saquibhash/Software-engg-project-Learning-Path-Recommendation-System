<template>
  <div class="container">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
  
  <div class="container text-center mt-5">
    <div class="card">
      <div class="card-body">
        <h1 class="mb-4">Welcome to Learning Path Recommendation App</h1>
        <div class="row justify-content-center">
          <div class="col-md-4">
            <div class="card">
              <div class="card-body">
                <router-link to="/userLogin" class="btn btn-primary btn-lg btn-block">
                  <b>Click for user login</b>
                </router-link>
              </div>
            </div>
          </div>

          <div class="col-md-4">
            <div class="card">
              <div class="card-body">
                <router-link to="/admin" class="btn btn-success btn-lg btn-block">
                  <b>Click for admin login</b>
                </router-link>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>

  </div>
  <!-- </div> -->
</template>

<script>
export default {
  name: "LoginView",
  data() {
    return {
      user: {
        email: "",
        password: "",
      },
    };
  },
  methods: {
    login() {
            this.$store.dispatch('loginUser',{email: this.user.email, password: this.user.password})
    },
  },
};
</script>
