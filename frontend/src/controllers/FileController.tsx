import axios from "axios";

const api = "http://localhost:81";


export async function ListFiles() {
    return axios
      .get(api + "/api/files/", {})
      .then((res) => {
        return res.data;
      })
      .catch((err) => {
        if (err.request){
          return [];
        }else{
          return err.response
        }

      });
  }

  export async function InsertNewFile(file: Blob, filename?: string) {

    const formData = new FormData();
    formData.append("file", file, filename)

    return axios
      .post(api + "/api/files/",
        formData, { headers: { 'Content-Type': 'multipart/form-data' } })
      .then((res) => {
        return res.data;
      })
      .catch((err) => {
        return err.response;
      });
  }

