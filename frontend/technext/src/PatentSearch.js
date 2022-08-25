import axios from "axios";

const SERVER_URL = "http://148.75.243.252:8080";

export const PatentsApi = axios.create({
  baseURL: SERVER_URL,
  responseType: "json"
});

export const getPatentResults = (value) => {
  return PatentsApi.post("", { query: value }).then(({ data }) => {
    if (data !== undefined) {
      return data;
    } else {
      console.error("No data for patent search.")
      return null;
    }
  });
 }