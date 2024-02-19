<template>
  <UserNavComponent>
    <div class="container">
      <div class="row justify-content-center">
        <div><h1>Completed Courses</h1></div>
        <div style="padding-bottom: 100px;"></div>
      </div>
      </div>

        <div class="row" v-if="Object.keys(courses).length > 0">

                    <div class="col-sm-12">
                      <table class="table">
                            <thead>
                              <tr>
                                <th scope="col">Subject</th>
                                <th scope="col">Level</th>
                                <th scope="col">Score</th>
                                <th scope="col">Grade</th>
                                <th scope="col">Rating</th>
                                <th scope="col">Feedback</th>
                              </tr>
                            </thead>

                            <tbody>
                                <tr class="col-sm-12" v-for="course in courses" :key="course.id">
                                  <th scope="row">{{ course.subject }}</th>
                                  <td>{{ course.level }}</td>
                                  <td>{{ course.score }}</td>
                                  <td>{{ course.finalGrade }}</td>
                                  <td><input id="rating" type="number" class="form-control" name="rating" v-model="course.rating" min = 1 max = 5
                                              @keyup.enter="updateRating(course)" required /></td>
                                  <td v-if="!course.editingFeedback"><input  type="text" v-model="course.feedback"
                                          @keydown.enter="toggleEditing(course, 'feedback')"></td>
                                  <td v-else >
                                    <span @keydown.enter="toggleEditing(course, 'feedback')">{{ course.feedback }}</span>

                                  </td>
                                  <b-button v-on:click="updateRating(course)" >
                                    Submit</b-button>
                                </tr>
                            
                            </tbody>
                      </table>  

























                        <!-- <div class="row">
                    
                            <div class="col-sm-4">
                              <b>Subject</b>
                            </div>
                            <div class="col-sm-3">
                              <b>Level</b>
                            </div>
                            <div class="col-sm-3">
                              <b>Score</b>
                            </div>
                            <div class="col-sm-3">
                              <b>Grade</b>
                            </div>

                        </div> -->
                  
                    </div> 
          
          <!--
          <div class="col-sm-12" v-for="course in courses" :key="course.id">
            <ul>
              <div class="row">
                <div class="col-sm-4">
                  {{ course.subject }}
                </div>
                <div class="col-sm-2">
                  {{ course.level }}
                </div>
                <div class="col-sm-1">
                  {{ course.score }}
                </div>
                <div class="col-sm-1">
                  {{ course.finalGrade }}
                </div>
                 <div class="col-sm-2">
                  <input v-if="!course.editingFeedback" type="text" v-model="course.feedback"
                    @keydown.enter="toggleEditing(course, 'feedback')">
                  <span v-else @keydown.enter="toggleEditing(course, 'feedback')">{{ course.feedback }}</span>
                </div>

                <div class="col-sm-2">
                  <div class="form-group row">
                    <input id="feedback" type="text" class="form-control" name="feedback" v-model="course.feedback"
                      required />
                  </div>
                </div>
                <div class="col-sm-2">
                  <div class="form-group row">
                    <input id="rating" type="number" class="form-control" name="rating" v-model="course.rating" min = 1 max = 5
                    @keyup.enter="updateRating(course)" required />
                  </div>
                </div>
              </div>
            
          
            <hr>
            -->

        </div>
        
      <!-- </div> -->

</UserNavComponent>
</template>

<script>
import { mapGetters } from "vuex";

export default {
  name: "UserCompletedCourses",
  data() {
    return {
      //get the profile details and disply it.
    };
  },
  methods: {
    updateRating(course){
      this.$store.dispatch('updateRating',{email: this.userData.email, subject : course.subject, rating: course.rating, feedback: course.feedback,})

    }
  },
  computed: {
    ...mapGetters(["getCoursesData","getUserData"]),
    courses() {
      return this.getCoursesData;
    },
    userData() {
      return this.getUserData[0];
    },
  },

};
</script>
<style></style>
