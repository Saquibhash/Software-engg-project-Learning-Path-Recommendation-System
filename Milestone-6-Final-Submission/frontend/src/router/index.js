import Vue from 'vue'
import VueRouter from 'vue-router'
import UserRegisterView from '../views/UserRegisterView.vue'
import UserLoginView from '../views/UserLoginView.vue'
import AdminLoginView from '../views/AdminLoginView.vue'
import UserProfile from '../views/UserProfile.vue'
import UploadData from '../views/UploadData.vue'
import UploadUserData from '../views/UploadUserData.vue'
import CreateNewUser from '../views/CreateNewUser.vue'
import UserCompletedCourses from '../views/UserCompletedCourses.vue'
import UserRecommendation from '../views/UserRecommendation.vue'
import MainPage from '../views/MainPage.vue'

import axios from 'axios'
import store from '../store'
Vue.use(VueRouter)

const routes = [
  {
    path: '/userProfile',
    name: 'UserProfile',
    component: UserProfile,
  },
  
  {
    path: '/uploadData',
    name: 'UploadData',
    component: UploadData,
  },
  {
    path: '/uploadUserData',
    name: 'UploadUserData',
    component: UploadUserData,
  },
  
  {
    path: '/createNewUser',
    name: 'CreateNewUser',
    component: CreateNewUser,
  },

  {
    path: '/userCourses',
    name: 'UserCompletedCourses',
    component: UserCompletedCourses,
    beforeEnter: (to, from, next) => {
      const email = store.getters.getUserData[0]['email']
      console.log(email);
      axios.get(`http://127.0.0.1:8080/user/courses/${email}`)
        .then(response => {
          console.log("response", response.data);
          store.commit('setCoursesData',response.data.courses);
          next()
        })
        .catch(error => {
          console.log(error)
        })
      next()
    }
  },
  

  {
    path: '/userRec',
    name: 'UserRecommendation',
    component: UserRecommendation,
    beforeEnter: (to, from, next) => {
      store.commit('clearRecommendedCourses');

      const level = store.getters.getUserData[0]['level']
      const email = store.getters.getUserData[0]['email']
      console.log(level);
      axios.get(`http://127.0.0.1:8080/courses/${level}/${email}`)
        .then(response => {
          console.log("response", response.data);
          store.commit('setLevelCourses',response.data.All_courses);
          store.commit('setCompletedCourses',response.data.Completed_courses);
          store.commit('setRemainingCourses',{ all: response.data.All_courses, completed: response.data.Completed_courses });
          next()
        })
        .catch(error => {
          console.log(error)
        })
      next()
    },
  },
  {
    path: '/logoutUser',
    name: 'UserLoginView',
    component: UserLoginView,
    beforeEnter: (to, from, next) => {
      store.commit('clearData');
      next()
    },
  },
  {
    path: '/logoutAdmin',
    name: 'AdminLoginView',
    component: AdminLoginView,
    beforeEnter: (to, from, next) => {
      store.commit('clearData');
      next()
    },
  },

  {
    path: '/admin',
    name: 'AdminLoginView',
    component: AdminLoginView
  },

  {
    path: '/',
    name: 'MainPage',
    component: MainPage
  },
  {
    path: '/userLogin',
    name: 'UserLoginView',
    component: UserLoginView
  },
  {
    path: '/Signup',
    name: 'UserRegisterView',
    component: UserRegisterView
  },
]

const router = new VueRouter({
  routes
})

export default router

