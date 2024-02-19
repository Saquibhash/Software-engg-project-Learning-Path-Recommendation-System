<template>
    <b-jumbotron class="jumbotron-non-scrollable">
        <div class="login-page">
            <div class="image-column"> 
                <!-- <img width="500" src="https://i.pinimg.com/564x/b8/8c/20/b88c20a36a4255e0729c6e27e89f03c3.jpg" alt="Movies ticket" /> -->
             </div>
            <div class="form-column">
                <b-jumbotron class="jumbotron-non-scrollable">
                    <div class="container">
                        <b-card>
                            <template #header>
                                <!-- <div class="text-center"> <span><img src="../assets/login.png" alt="login"
                                            height="75" /></span>
                                </div> -->
                                <div class="text-center"> <span>STUDENT LOGIN</span>
                                </div>
                            </template>
                            <b-card-text>
                                <form @keydown.enter.prevent="userLogin">
                                    <div class="form-group row">
                                        <label for="userId" class="col-md-4 col-form-label text-md-right"><b>User
                                                Id</b></label>

                                        <div class="col-md-6">
                                            <input id="userId" type="text" class="form-control" name="userId"
                                                v-model="user.email" placeholder="user@email.com" required autofocus />
                                        </div>
                                    </div>
                                    <div class="form-group row">
                                        <label for="password"
                                            class="col-md-4 col-form-label text-md-right"><b>Password</b></label>

                                        <div class="col-md-6">
                                            <input id="password" type="password" class="form-control" name="password"
                                                v-model="user.password" placeholder="*********" required />
                                        </div>
                                        
                                        <div class="text-right">
                                            <b-button type="submit" class="btn btn-dark d-grid" @click.prevent="userLogin">Login</b-button> 
                                        </div>
                                    </div>
   
                                </form>
                                <b-spinner v-if="$store.state.generateotp"></b-spinner>
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
export default {

    name: "UserLoginView",
    data() {
        return {
            user: {
                email: "",
                password: "",
                role:"USER",
            },
        };
    },
    methods: {
        userLogin() {
            this.$store.dispatch('login', { email: this.user.email, password: this.user.password , role:this.user.role })
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
    background-image: '' ;
}

.image-column {
    flex: 1;
}

.form-column {
    flex: 1;
    border-left: 1px solid #ccc;
}

.jumbotron-non-scrollable {
    overflow: hidden;
}</style>
  