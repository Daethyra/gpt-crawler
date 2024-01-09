import { Config } from "./src/config";

export const defaultConfig: Config = {
  url: "https://python.langchain.com/docs/get_started/introduction",
  match: [
    "https://python.langchain.com/docs/**",
  ],
    maxPagesToCrawl: 100,
  outputFileName: "output.json",
};
