<template>
  <UserNavComponent>
    <div class="container">

      <b-jumbotron class="jumbotron-non-scrollable">
          <b-card>

            <template #header>
              <div class="text-center"><h1>Profile</h1></div>
            </template>

            <b-card-text>
              <form ref="form" @submit.stop.prevent="submitForm">
                <div class="row mb-2">
                  <div class="col-6">
                    <b-form-label>Name</b-form-label>
                    <b-form-input id="Name" class="form-control form-control-lg" placeholder="Name"
                      v-model="user.name" disabled></b-form-input>
                  
                    </div>
                </div>
                <b-form-label>Email</b-form-label>
                <div class="row mb-2">
                  <div class="col-12"><b-form-input id="email" v-model="user.email" type="email"
                      placeholder="user@gmail.com" disabled required></b-form-input></div>
                </div>
                <b-form-label>Date of Birth</b-form-label>
                <div class="row mb-2">
                  <div class="col-6"><b-form-datepicker id="dob" :show-decade-nav="true" disabled placeholder="Enter date of birth" v-model="user.dob" required></b-form-datepicker></div>
                  <div class="col-6">

                    
                    <b-form-group>
                      <b-form-label>Gender</b-form-label>
                      <b-form-radio-group v-model="user.gender" :options="gender_options" disabled></b-form-radio-group>
                    </b-form-group>
                  </div>
                </div>
                
                <div class="row mb-2">
                  <div class="col-6">
                    <b-form-label>CGPA</b-form-label>
                    <b-form-input id="cgpa" class="mb-2 mr-sm-2 mb-sm-0" placeholder="Cgpa"
                    v-model="user.cgpa" disabled></b-form-input>
                  </div>
                </div>
                

                <div style="margin-top: 4%;">
                <!-- <p><strong>about me:</strong> {{ user.aboutMe }}</p> -->
                <!-- <p>current city: {{ user.courses }}</p> -->
                <p><strong>Is this only degree?:</strong> {{ user.onlyDegree }}</p>
                <div><strong>Current Courses:</strong>  {{ user.courses }}</div>
              </div>

                <div class="row mb-2" v-if="edit_profile">
                  <div class="col-6">
                    <b-form-checkbox id="onlyDegree" v-model="user.onlyDegree" name="onlyDegree" value="True"
                      unchecked-value="False" v-bind="user.onlyDegree">Only Degree</b-form-checkbox>
                  </div>
                </div>
                <div class="row mb-2">
                  <div class="col-6" >
                    <b-form-textarea v-if="edit_profile" label="About Me:" id="aboutMe" v-model="user.aboutMe" placeholder="About me......" rows="3" max-rows="6"></b-form-textarea>
                  </div>
                </div>
                
                <!-- <div class="row mb-2">
                  
                  <div class="col-6" v-if="edit_profile">
                    <b-form-group label="City:">
                      <b-form-select v-model="user.courses" :options="courses_options" multiple :select-size="4"
                      required></b-form-select>
                    </b-form-group>
                  </div>
                </div> -->
                
                
                <div class="row mb-2" v-if="edit_profile">
                  <div class="col-1">
                    <button type="submit" class="btn btn-primary">Submit</button>
                  </div>
                </div>
                <!-- <button v-else class="btn btn-primary" @click="toggle_edit()">edit profile</button> -->
                
              </form>
            </b-card-text>
          </b-card>
        
      </b-jumbotron>
    </div>
  </UserNavComponent>
</template>

<script>
import { mapGetters } from "vuex";

export default {
  name: "UserProfile",
  data() {
    return {
      isSubmitted: false,
      edit_profile: false,
      user: {
        name: "",
        dob: "",
        email: "",
        gender: "",
        onlyDegree: false,
        courses: [],
        aboutMe: "",
        cgpa:"",
      },

      courses_options: [{ value: 'Mumbai', text: 'Mumbai' },
      { value: 'Chennai', text: 'Chennai' },
      { value: 'Bangalore', text: 'Bangalore' },
      { value: 'Hyderabad', text: 'Hyderabad' },
      { value: 'Patna', text: 'Patna' },
      { value: 'Delhi', text: 'Delhi' },
      ],
      
      
      gender_options: [{ value: 'Female', text: 'Female' },
      { value: 'Male', text: 'Male' },
      ],


    };
  },
  methods: {
    submitForm() {

      this.edit_profile = false;
      console.log(this.user);
      this.$store.dispatch('submitProfileDetails', { 
        name: this.user.name, 
        dob: this.user.dob , 
        email:this.user.email,
        gender:this.user.gender, 
        onlyDegree:this.user.onlyDegree,
        // courses:this.user.courses,
        aboutMe:this.user.aboutMe,
        cgpa: this.user.cgpa,
       })
        },
      toggle_edit() {
        this.edit_profile = !this.edit_profile
      }

  },
  computed: {
    ...mapGetters(["getUserData"]),
    userData() {
      return this.getUserData[0];
    },
  },
  created() {
  if (this.userData) {
    this.user.name = this.userData.name || "";
    this.user.dob = this.userData.dob || "";
    this.user.email = this.userData.email || "";
    this.user.gender = this.userData.gender || "";
    this.user.onlyDegree = this.userData.onlyDegree || false;
    this.user.aboutMe = this.userData.aboutMe || "";
    this.user.courses = this.userData.courses || [];
    this.user.cgpa = this.userData.cgpa || "";
}}

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