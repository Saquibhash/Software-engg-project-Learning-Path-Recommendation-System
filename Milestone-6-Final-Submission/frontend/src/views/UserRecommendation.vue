<template>
  <UserNavComponent>

    <div class="container">
          <div style="text-align: center;padding-top: 100px;">
          <h1>Course Recommendation</h1>
          </div>
          
          <div style="padding-bottom: 100px;"></div>
          <form @submit.prevent="recommend">
            <div class="form-group">
                    <div><h4 style="color: Tomato;text-align: center;">   Please give your preferences : </h4></div>
                    <div style="padding-bottom: 50px;"></div>
                    <label for="domain" class="col-md-4">Domain: </label>
                    <div class="col-md-6">
                      <b-form-select id="domain" v-model="rec.domain" placeholder="Select Domain">
                      <b-form-select-option disabled value="Select Domain">Select Domain</b-form-select-option>
                      <b-form-select-option @click="selectDomain('Data science')" value="Data science">Data
                            science</b-form-select-option>
                      <b-form-select-option @click="selectDomain('Programming')"
                            value="Programming">Programming</b-form-select-option>
                      </b-form-select> 
                    </div>
                  </div>
                  <div class="form-group">
                    <label class="col-md-4" for="hours">No.of hours per week:</label>
                    <div class="col-md-6">
                      <input id="hours" type="number" class="form-control" name="number" v-model="rec.hours" min="10" max="40"
                        required />
                    </div>
                  </div>
                  <div class="form-group">
                    <label for="count" class="col-md-4">Max subjects:</label>
                    <div class="col-md-6">
                      <input id="count" type="number" class="form-control" name="number" v-model="rec.count" min="1" max="4"
                        required />
                    </div>
                  </div>
                  <div class="form-group">
                    <div class="col-md-6" style="padding-top: 20px;text-align: right;">
                      <button type="submit" class="btn btn-primary">Generate Recommendation</button>
                    </div>
                  </div>
            </form>
        </div>

<!-- convert this to table -->




        <div class="row" v-if="recommendedCourses && recommendedCourses.length > 0" style="text-align: left;padding-top: 100px;">
          <div class="container">
            <div class="col-sm-12">
              <h4 style="color: Tomato;text-align: center;">Here is your course recommendation :</h4>
              <div style="padding-bottom: 50px;"></div>
                      <table class="table">
                            <thead>
                              <tr>
                                <th scope="col">Subject</th>
                                <th scope="col">Student's Avg Rating</th>
                                <th scope="col">Student's Avg Weekly hours</th>
                                <th scope="col">Student's Avg Score</th>
                                <!-- <th scope="col">Max Student's Grade</th> -->
                              </tr>
                            </thead>

                            <tbody>
                              
                              
                                <tr class="col-sm-12" v-for="(course, index) in recommendedCourses" :key="index">
                                  <th scope="row">{{ course.subject }}</th>
                                  <td>{{ course.average_rating }}</td>
                                  <td>{{ course.average_weekly_hrs }}</td>
                                  <td>{{ course.score }}</td>
                                  <!-- <td>{{ course.finalGrade }}</td> -->
                                </tr>
                            
                            </tbody>
                      </table> 
            </div>


      <!--
            <div class="col-sm-3">
              <h4>Subject</h4>
            </div>
            <div class="col-sm-2">
              <h4>Student's Avg Rating</h4>
            </div>
            <div class="col-sm-2">
              <h4>Student's Avg Weekly hours</h4>
            </div>
            <div class="col-sm-2">
              <h4>Student's Avg Score</h4>
            </div>
            <div class="col-sm-2">
              <h4>Max student's grade</h4>
            </div> 
        </div>

        <div class="row" v-for="(course, index) in recommendedCourses" :key="index">
          <div class="col-sm-3">
            {{ course.subject }}
          </div>
          <div class="col-sm-2">
            {{ course.average_rating }}
          </div>
          <div class="col-sm-2">
            {{ course.average_weekly_hrs }}
          </div>
          <div class="col-sm-2">
            {{ course.score }}
          </div>
          <div class="col-sm-2">
            {{ course.finalGrade }}
          </div> 
        -->
        </div>
        </div>
    
  </UserNavComponent>
</template>

<script>
import { mapGetters } from "vuex";
import axios from 'axios';
import store from '../store'


export default {
  name: "UserRecommendation",
  data() {
    return {
      rec: {
        degree: false,
        hours: 0,
        domain: 'Select Domain',
        count: 0,
        remCourses: null,
      },
    };
  },
  methods: {
    recommend() {
      console.log("Before", this.remainingCourses);
      if (this.rec.domain != null) { // and number in limit # and rest 
        this.rec.remCourses = this.remainingCourses.filter(course => course.category.toLowerCase().trim() === this.rec.domain.toLowerCase().trim());
        console.log("After", this.rec.remCourses);
        axios.post("http://127.0.0.1:8080/user/generateRecommendation", {
          domain: this.rec.domain,
          hours: this.rec.hours,
          degree: this.rec.degree,
          courses: this.rec.remCourses,
          count: this.rec.count,
        })
          .then((response) => {
            store.commit('setRecommendedCourses', response.data.recommended_courses);
            this.$router.push('/userRec');
          })
          .catch((error) => {
            console.error(error);
          });
      } else {
        console.error("Domain not selected");
      }
    },


    selectDomain(domain) {
      this.rec.domain = domain;
    }
  },
  computed: {
    ...mapGetters(["getUserData", 'getRemainingCourses', 'getRecommendedCourses']),
    userData() {
      return this.getUserData[0].onlyDegree;
    },
    remainingCourses() {
      return this.getRemainingCourses;
    },
    recommendedCourses() {
      return this.getRecommendedCourses;
    }
  },

};
</script>
<style></style>
