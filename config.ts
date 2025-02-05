import { Config } from "./src/config";

export const defaultConfig: Config = {
  url: "https://python.langchain.com/docs/introduction/",
  match: [
    "https://python.langchain.com/docs/**",
  ],
    maxPagesToCrawl: 20,
  outputFileName: "output.json",
};
