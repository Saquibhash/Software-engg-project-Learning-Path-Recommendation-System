import router from '@/router'
import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    coursesData: "",
    otp: false,
    generateotp: false,
    loggedInUserName: "",
    profilePicture: "",
    userData: {},
    levelCourses: {},
    completedCourses: {},
    remainingCourses: {},
    recommendedCourses: {},
  },
  getters: {
    getCoursesData: (state) => {
      return state.coursesData
    },
    getOTP: (state) => {
      return state.otp
    },
    getUserName: (state) => {
      return state.loggedInUserName
    },
    getUserData: (state) => {
      return state.userData
    },
    getLevelCourses: (state) => {
      return state.levelCourses
    },
    getCompletedCourses: (state) => {
      return state.completedCourses
    },
    getRemainingCourses: (state) => {
      return state.remainingCourses
    },
    getRecommendedCourses: (state) => {
      return state.recommendedCourses
    },
  },
  mutations: {
    setCoursesData: (state, data) => {
      state.coursesData = data;
    },
    setOTP: (state, data) => {
      state.otp = data
    },
    setLevelCourses: (state, data) => {
      state.levelCourses = data;
    },
    setUserData: (state, data) => {
      state.userData = data;
    },
    setCompletedCourses: (state, data) => {
      state.completedCourses = data;
    },

    setRemainingCourses(state, { all, completed }) {

      const completedSubjects = new Set(completed.map(course => course.subject));
      state.remainingCourses = all.filter(course => !completedSubjects.has(course.name));
      console.log(state.remainingCourses);

    },
    setRecommendedCourses: (state, data) => {
      state.recommendedCourses = data;
    },
    clearRecommendedCourses: (state) => {
      state.recommendedCourses = {};
    },
    clearData: (state) => {
      state.recommendedCourses = {};
      state.coursesData= "";
      state.otp= false;
      state.generateotp= false;
      state.loggedInUserName= "";
      state.profilePicture= "";
      state.userData= {};
      state.levelCourses= {};
      state.completedCourses= {};
      state.remainingCourses= {};
      state.recommendedCourses= {};
    },
  },
  actions: {

    async login({ commit }, payload) {
      axios.post("http://127.0.0.1:8080/user/login", payload)
        .then((response) => {
          console.log(response.data.user_detail);

          if (response.data.role == 'USER') {
            commit('setUserData', response.data.user_detail)
            router.push('/userProfile')
          }
          else if (response.data.role == 'ADMIN') {
            router.push('/uploadData')
          }
        })
        .catch((error) => {
          console.error(error);
        });

    },
       async updateRating({ commit }, payload) {
      axios.put("http://127.0.0.1:8080/user/rating", payload)
        .then((response) => {
          commit('setCoursesData',response.data.courses);
          router.push('/userCourses')
        })
        .catch((error) => {
          console.error(error);
        });

    },
    async uploadCSVData({ commit }, payload) {
      axios.post("http://127.0.0.1:8080/admin/uploadData", payload)
        .then((response) => {
          commit('setgeneratingotp', false);
          console.log(response.data);
          alert('successfully uploaded')
          router.push('/uploadData')
        })
        .catch((error) => {
          alert('try again')
          console.error(error);
        });
    },

    async uploadUserCSVData({ commit }, payload) {
      axios.post("http://127.0.0.1:8080/admin/userData", payload)
        .then((response) => {
          commit('setgeneratingotp', false);
          console.log(response.data);
          alert('successfully uploaded')
          router.push('/uploadUserData')
        })
        .catch((error) => {
          alert('try again')
          console.error(error);
        });
    },

    async submitProfileDetails({ commit }, payload) {
      console.log(payload)
      axios.put("http://127.0.0.1:8080/user/updateProfile", payload)
        .then((response) => {
          commit('setgeneratingotp', false);
          console.log(response.data);
          commit('setUserData', response.data.user_detail)
          router.push('/userProfile')
        })
        .catch((error) => {
          console.error(error);
        });
    },

  },
  modules: {
  }
})
