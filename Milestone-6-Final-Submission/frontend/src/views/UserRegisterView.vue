<template>
    <b-jumbotron class="jumbotron-non-scrollable">
        <div class="register-page">
            <div class="form-column">
                <b-jumbotron class="jumbotron-non-scrollable">
                    <div class="container">
                        <b-card>
                            <template #header>
                                <div class="text-center"> <span><img src="../assets/register.png" alt="register"
                                            height="75" /></span>
                                </div>
                            </template>
                            <b-card-text>
                                <form @submit.enter.prevent="sendOTP">
                                    <div class="row mb-2">
                                        <div class="col-6"><b-form-input id="FirstName" class="mb-2 mr-sm-2 mb-sm-0"
                                                placeholder="First Name" v-model="user.firstName"></b-form-input></div>
                                        <div class="col-6"><b-form-input id="LastName" class="mb-2 mr-sm-2 mb-sm-0"
                                                placeholder="Last Name" v-model="user.lastName"></b-form-input></div>
                                    </div>
                                    <div class="row mb-2">
                                        <div class="col-12"><b-form-input id="email" v-model="user.email" type="email"
                                                placeholder="user@gmail.com" :disabled="isSubmitted"
                                                required></b-form-input></div>
                                    </div>
                                    <div class="row mb-2">
                                        <div class="col-6"><b-form-input id="password" class="mb-2 mr-sm-2 mb-sm-0"
                                                type="password" placeholder="Enter Password" v-model="user.password"
                                                :disabled="isSubmitted"></b-form-input></div>
                                        <div class="col-6"><b-form-input id="reenterpassword" class="mb-2 mr-sm-2 mb-sm-0"
                                                type="password" placeholder="Re-enter Password" v-model="user.rePassword"
                                                :disabled="isSubmitted"></b-form-input>
                                        </div>
                                    </div>
                                    <div class="row mb-2">
                                        <div class="col-6"><b-form-datepicker id="dob" :show-decade-nav=true
                                                placeholder="Enter date of birth" v-model="user.dob"
                                                required></b-form-datepicker></div>
                                        <div class="col-6">
                                            <b-form-select v-model="user.city"  required>
                                            <b-form-select-option v-for="city in city_options" :value="city.value"
                                                :key="city.value">
                                                {{ city.text }}
                                            </b-form-select-option>
                                        </b-form-select>
                                        </div>
                                    </div>
                                    <div class="row mb-2">
                                        <div class="col-1">
                                            <button type="submit" class="btn btn-primary">Register</button>
                                        </div>
                                    </div>
                                </form>
                                <form @keydown.enter.prevent="validateOTP">
                                    <b-spinner v-if="$store.state.generateotp"></b-spinner>
                                    <div v-if="showOTP === true">
                                        <div class="form-group row">
                                            <label for="otp" class="col-md-4 col-form-label text-md-right"></label>
                                            <div class="col-md-6">
                                                <p class="text-justify text-success">Check your Email for OTP..</p>
                                            </div>
                                        </div>
                                        <div class="form-group row">
                                            <label for="otp"
                                                class="col-md-4 col-form-label text-md-right"><b>OTP</b></label>
                                            <div class="col-md-6">
                                                <input id="otp" type="text" class="form-control" name="otp"
                                                    v-model="user.otp" required autofocus />
                                            </div>
                                        </div>
                                    </div>
                                </form>
                            </b-card-text>
                        </b-card>
                    </div>
                </b-jumbotron>
            </div>
        </div>
    </b-jumbotron>
</template>
  
<script>
import { mapGetters } from "vuex";
import axios from 'axios';

export default {

    name: "UserRegisterView",
    data() {
        return {
            isSubmitted: false,
            user: {
                firstName: '',
                lastName: '',
                email: "",
                password: "",
                rePassword: "",
                dob: '',
                gender: '',
                city: '',
                otp: '',
            },
            city_options: [{ value: 'Mumbai', text: 'Mumbai' },
            { value: 'Chennai', text: 'Chennai' },
            { value: 'Bangalore', text: 'Bangalore' },
            { value: 'Hyderabad', text: 'Hyderabad' },
            { value: 'Patna', text: 'Patna' },
            { value: 'Delhi', text: 'Delhi' },
            ],

        };
    },
    methods: {
        sendOTP() {
            console.log("sendOTP");
            this.$store.commit('setOTP', true);
            this.$store.dispatch('sendOTP', { userId: this.user.email })
        },
        validateOTP() {
            console.log("validateOTP")
            axios.get(`http://127.0.0.1:8080/user/validateOTP/${this.user.email}/${this.user.otp}`)
                .then((response) => {
                    console.log("validating OTP done", response);
                    this.$store.dispatch('userRegister', { firstName: this.user.firstName, lastName: this.user.lastName, email: this.user.email, password: this.user.password, dob: this.user.dob, city: this.user.city })
                    this.$store.commit('setOTP', false);
                })
                .catch((error) => {
                    //do something if the OTP is invalid.
                    console.error(error.response.data);
                });
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
.register-page {
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
}

.jumbotron-non-scrollable {
    overflow: hidden;
}
</style>
  