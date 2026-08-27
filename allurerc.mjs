import { env } from "node:process";

export default {
  name: "Dummy App Test Report",
  output: "./allure-report",
  plugins: {
    awesome: {
      options: {
        publish: true,
        singleFile: true,
      },
    },
    dashboard: {
      options: {
        publish: true,
        singleFile: true,
        reportName: "Dashboard",
      },
    },
  },
  allureService: {
    accessToken: env.ALLURE_ACCESS_TOKEN
  },
};
