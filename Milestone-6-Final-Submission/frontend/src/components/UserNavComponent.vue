<template>
        <div class="d-flex">
            
            <div class="b-example-divider b-example-vr sidebar"></div>
            
            <div class="d-flex flex-column flex-shrink-0 " style="width: 280px">
                <b-nav vertical class="w-35 sidebar">
                    <div style="padding-bottom: 100px;"></div>
                    <b-nav-item>
                        <router-link to="/userProfile" class="nav-link link-dark">
                            <span class="icon-text">
                                <i class="fa-solid fa-user"></i> Profile
                            </span>
                        </router-link>
                    </b-nav-item>
                    <b-nav-item>
                        <router-link to="/userCourses" class="nav-link link-dark">
                            <span class="icon-text">
                                <i class="fa-solid fa-list"></i> Completed Courses
                            </span>
                        </router-link>
                    </b-nav-item>
                    <b-nav-item>
                        <router-link to="/userRec" class="nav-link link-dark">
                            <span class="icon-text">
                                <i class="fa-solid fa-ticket"></i> Recommendation
                            </span>
                        </router-link>
                    </b-nav-item>

                    <b-nav-item>
                        <router-link to="/logoutUser" class="nav-link link-dark">
                            <span class="icon-text">
                                <i class="fa-solid fa-right-from-bracket"></i> Logout
                            </span>
                        </router-link>
                    </b-nav-item>
                </b-nav>
            </div>
            <div class="b-example-divider b-example-vr"></div>
            <div class="flex-grow-1 overflow-auto">
                <slot></slot>
            </div>
            <div class="b-example-divider b-example-vr"></div>
        </div>

</template>
  
<script>
export default {
    name: "UserNavComponent",
};
</script>
  
<style scoped>
.sidebar {
    position: fixed;
    top: 0;
    bottom: 0;
    overflow-y: auto;
}




.nav-item-with-gap {
    margin-left: 10px;
}

.icon-text {
    display: flex;
    align-items: center;
}

.icon-text .fa-solid {
    margin-right: 7px;
}


.b-example-divider {
    /* height: 3rem; */
    /* background-color: rgba(0, 0, 0, 0.1); */
    border: solid rgba(0, 0, 0, 0.15);
    border-width: 1px 0;
    box-shadow: inset 0 0.5em 1.5em rgba(0, 0, 0, 0.1),
        inset 0 0.125em 0.5em rgba(0, 0, 0, 0.15);
        overflow: auto;

}

.b-example-vr {
    flex-shrink: 0;
    width: 1.5rem;
    height: 100vh;
    overflow: auto; 

}

.overflow-auto {
  overflow: auto;
}
</style>