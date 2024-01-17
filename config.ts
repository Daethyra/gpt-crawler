import { Config } from "./src/config";

export const defaultConfig: Config = {
  url: "https://js.langchain.com/docs/get_started/introduction",
  match: [
    "https://js.langchain.com/docs/**",
  ],
    maxPagesToCrawl: 50,
  outputFileName: "output.json",
};
