<!-- <template>
    <AdminNavComponent>
        <div class="container">
            <div class="row justify-content-center">
                <form ref="form" @submit.stop.prevent="submitForm">
                    <b-form-file v-model="form.file" accept=".csv" :state="Boolean(form.file)"
                        placeholder="Choose a CSV file " drop-placeholder="Drop CSV file here..."
                        @change="handleFileUpload"></b-form-file>
                    <b-button type="submit" variant="primary">Publish</b-button>
                </form>
                <div>
                </div>
            </div>
        </div>
    </AdminNavComponent>
</template>

<script>

export default {
    name: "UploadData",
    data() {
        return {
            form: {
                file: null,
            },
        };
    },
    methods: {
        submitForm() {
            if (this.form.file) {
                console.log("Is it workinggging");
                const reader = new FileReader();
                reader.readAsDataURL(this.form.file);
                reader.onload = () => {
                    console.log(reader.result.split(",")[1]);
                    this.$store.dispatch("uploadCSVData", {
                        file: reader.result.split(",")[1],
                    }).then(() => {});
                };
            } else {
                console.log("File is not selected.");
            }
        },
    },

};
</script>
<style></style> -->


<template>
    <AdminNavComponent>
        <div class="container">
          <div style="text-align: center;padding-top: 100px;">
          <h1>Upload User Data</h1>
          </div>

            <div class="row justify-content-center" style="text-align: center;padding-top: 100px;">
                <form ref="form" @submit.stop.prevent="submitForm">

                    <b-form-file v-model="form.file" accept=".csv" :state="Boolean(form.file)"
                        placeholder="Choose a CSV file " drop-placeholder="Drop CSV file here..."
                        @change="handleFileUpload"></b-form-file>

                        <div style="margin-top: 20px;">
                          <!-- Your content here -->
                          </div>
                    <b-button type="submit" variant="primary" :disabled="isUploading">Upload</b-button>
                </form>
                <div v-if="isUploading" class="text-center">
                    <b-spinner label="Uploading..."></b-spinner>
                </div>
            </div>
        </div>
    </AdminNavComponent>
</template>

<script>
export default {
    name: "UploadData",
    data() {
        return {
            form: {
                file: null,
            },
            isUploading: false,
        };
    },
    methods: {
        submitForm() {
            if (this.form.file) {
                this.isUploading = true;
                const reader = new FileReader();
                reader.readAsDataURL(this.form.file);
                reader.onload = () => {
                    this.$store.dispatch("uploadUserCSVData", {
                        file: reader.result.split(",")[1],
                    }).then(() => {
                        this.isUploading = false;
                    });
                };
            } else {
                console.log("File is not selected.");
            }
        },
    },
};
</script>
<style></style>
