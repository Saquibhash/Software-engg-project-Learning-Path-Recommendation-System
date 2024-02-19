<template>
    <b-jumbotron class="jumbotron-non-scrollable">  

    <b-alert variant="success"  v-if="isSubmitted"  @dismissed="dismissAlert" show>Success Alert</b-alert>

        <div class="login-page">
            <div class="image-column">
                <!-- <img width="500" src="https://i.pinimg.com/564x/b8/8c/20/b88c20a36a4255e0729c6e27e89f03c3.jpg" alt="Admin Login" /> -->
            </div>
            <div class="form-column">
                <b-jumbotron class="jumbotron-non-scrollable">
                    <div class="container">
                        <b-card>
                            <template #header>
                                <div class="text-center"> <span>ADMIN LOGIN</span>
                                </div>
                            </template>
                            <b-card-text>
                                <form @keydown.enter.prevent="validatingAdmin">
                                    <div class="form-group row">
                                        <label for="userId"
                                            class="col-md-4 col-form-label text-md-right"><b>UserId</b></label>

                                        <div class="col-md-6">
                                            <input id="userId" type="text" class="form-control" name="userId"
                                                v-model="user.userId" placeholder="admin@email.com"  required autofocus :disabled="isSubmitted"/>
                                        </div>
                                    </div>
                                    <div class="form-group row">
                                        <label for="password"
                                            class="col-md-4 col-form-label text-md-right"><b>Password</b></label>

                                        <div class="col-md-6">
                                            <input id="password" type="password" placeholder="*********"  class="form-control" name="password"
                                                v-model="user.password" required :disabled="isSubmitted"/>
                                        </div>

                                        <div class="text-right">
                                            <b-button class="btn btn-dark d-grid" v-on:click="validatingAdmin">Login</b-button> 
                                        </div>


                                    </div>
                                </form>
                              


                            </b-card-text>
                        </b-card>
                    </div>
                </b-jumbotron>
                <div class="row justify-content-center" style="margin-top: 3%;">
                    <router-link to="/" class="btn btn-dark d-grid">back to main page</router-link>
                </div>
            </div>
        </div>
    </b-jumbotron>
</template>
  
<script>
import { mapGetters } from "vuex";

export default {

    name: "AdminLoginView",
    data() {
        return {
            isSubmitted: false,
            user: {
                userId: "",
                password: "",
               role:"ADMIN",
            },
        };
    },
    methods: {
        validatingAdmin() {
            this.$store.dispatch('login', { email: this.user.userId, password: this.user.password , role:this.user.role })
        },
       
    },
    computed: {
        ...mapGetters(["getOTP"]),
        showOTP() {
            return this.getOTP;
        },
    },
};
</script>
<style scoped>
.login-page {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 75vh;
}

.image-column {
    flex: 1;
}

.form-column {
    flex: 1;
    border-left: 1px solid #ccc;
    /* Add this to create a vertical grey line */

}

.jumbotron-non-scrollable {
    overflow: hidden;
}
</style>