# GPT Crawler <!-- omit from toc -->

Crawl a site to generate knowledge files to create your own custom GPT from one or multiple URLs

![Gif showing the crawl run](https://github.com/BuilderIO/gpt-crawler/assets/844291/feb8763a-152b-4708-9c92-013b5c70d2f2)

- [Get started](#get-started)
  - [Running locally](#running-locally)
    - [Clone the repository](#clone-the-repository)
      - [Run in Docker Container](#docker-container--virtualize-the-run)
      - [Run on Host Operating System](#run-on-host-os)
        - [Install dependencies](#install-dependencies)
        - [Configure the crawler](#configure-the-crawler)
        - [Run your crawler](#run-your-crawler)
- [Upload your data to OpenAI](#upload-your-data-to-openai)
  - [Create a custom GPT](#create-a-custom-gpt)
  - [Create a custom assistant](#create-a-custom-assistant)
- [Contributing](#contributing)

## Get started

### Running locally

#### Clone the repository

```sh
git clone --recurse-submodules https://github.com/Daethyra/gpt-crawler
```


#### Docker Container | Virtualize the Run (Recommended method)

In my experience, the directions for using Docker by BuilderIO has never worked. However, the following instructions have never failed me.
1. In root dir, configure your `config.ts` and set the site you'd like to scrape along with the maximum number of pages to scrape.
2. Run:
  - In PowerShell: `docker build -t gpt-crawler . ; docker run -it gpt-crawler`
  - In Bash: `docker build -t gpt-crawler . && docker run -it gpt-crawler`
3. Wait for finish. The build and execution process will take care of the rest.
4. Once done, save the file 'gpt-crawler-curated_markdown.md' locally for retrieval augmented generation.
5. (Optional) Follow [the instructions below](./README.md#Upload-your-data-to-OpenAI) to create an AI Assistant via OpenAI hosting.


#### Run on Host OS

##### Install dependencies

```sh
npm i
```

##### Configure the crawler

Open [config.ts](config.ts) and edit the `url` and `selector` properties to match your needs.

E.g. to crawl the Builder.io docs to make our custom GPT you can use:

```ts
export const defaultConfig: Config = {
  url: "https://www.builder.io/c/docs/developers",
  match: "https://www.builder.io/c/docs/**",
  selector: `.docs-builder-container`,
  maxPagesToCrawl: 50,
  outputFileName: "output.json",
};
```

See [config.ts](src/config.ts) for all available options. Here is a sample of the common configuration options:

```ts
type Config = {
  /** URL to start the crawl, if sitemap is provided then it will be used instead and download all pages in the sitemap */
  url: string;
  /** Pattern to match against for links on a page to subsequently crawl */
  match: string;
  /** Selector to grab the inner text from */
  selector: string;
  /** Don't crawl more than this many pages */
  maxPagesToCrawl: number;
  /** File name for the finished data */
  outputFileName: string;
  /** Optional resources to exclude
   *
   * @example
   * ['png','jpg','jpeg','gif','svg','css','js','ico','woff','woff2','ttf','eot','otf','mp4','mp3','webm','ogg','wav','flac','aac','zip','tar','gz','rar','7z','exe','dmg','apk','csv','xls','xlsx','doc','docx','pdf','epub','iso','dmg','bin','ppt','pptx','odt','avi','mkv','xml','json','yml','yaml','rss','atom','swf','txt','dart','webp','bmp','tif','psd','ai','indd','eps','ps','zipx','srt','wasm','m4v','m4a','webp','weba','m4b','opus','ogv','ogm','oga','spx','ogx','flv','3gp','3g2','jxr','wdp','jng','hief','avif','apng','avifs','heif','heic','cur','ico','ani','jp2','jpm','jpx','mj2','wmv','wma','aac','tif','tiff','mpg','mpeg','mov','avi','wmv','flv','swf','mkv','m4v','m4p','m4b','m4r','m4a','mp3','wav','wma','ogg','oga','webm','3gp','3g2','flac','spx','amr','mid','midi','mka','dts','ac3','eac3','weba','m3u','m3u8','ts','wpl','pls','vob','ifo','bup','svcd','drc','dsm','dsv','dsa','dss','vivo','ivf','dvd','fli','flc','flic','flic','mng','asf','m2v','asx','ram','ra','rm','rpm','roq','smi','smil','wmf','wmz','wmd','wvx','wmx','movie','wri','ins','isp','acsm','djvu','fb2','xps','oxps','ps','eps','ai','prn','svg','dwg','dxf','ttf','fnt','fon','otf','cab']
   */
  resourceExclusions?: string[];
  /** Optional maximum file size in megabytes to include in the output file */
  maxFileSize?: number;
  /** Optional maximum number tokens to include in the output file */
  maxTokens?: number;
};
```

##### Run your crawler

```sh
npm start
```

## Upload your data to OpenAI

The crawl will generate a file called `output.json` at the root of this project. Upload that [to OpenAI](https://platform.openai.com/docs/assistants/overview) to create your custom assistant or custom GPT.

### Create a custom GPT

Use this option for UI access to your generated knowledge that you can easily share with others

> Note: you may need a paid ChatGPT plan to create and use custom GPTs right now

1. Go to [https://chat.openai.com/](https://chat.openai.com/)
2. Click your name in the bottom left corner
3. Choose "My GPTs" in the menu
4. Choose "Create a GPT"
5. Choose "Configure"
6. Under "Knowledge" choose "Upload a file" and upload the file you generated
7. if you get an error about the file being too large, you can try to split it into multiple files and upload them separately using the option maxFileSize in the config.ts file or also use tokenization to reduce the size of the file with the option maxTokens in the config.ts file

![Gif of how to upload a custom GPT](https://github.com/BuilderIO/gpt-crawler/assets/844291/22f27fb5-6ca5-4748-9edd-6bcf00b408cf)

### Create a custom assistant

Use this option for API access to your generated knowledge that you can integrate into your product.

1. Go to [https://platform.openai.com/assistants](https://platform.openai.com/assistants)
2. Click "+ Create"
3. Choose "upload" and upload the file you generated

![Gif of how to upload to an assistant](https://github.com/BuilderIO/gpt-crawler/assets/844291/06e6ad36-e2ba-4c6e-8d5a-bf329140de49)

## Contributing

Know how to make this project better? Send a PR!

<br>
<br>

<p align="center">
   <a href="https://www.builder.io/m/developers">
      <picture>
         <source media="(prefers-color-scheme: dark)" srcset="https://user-images.githubusercontent.com/844291/230786554-eb225eeb-2f6b-4286-b8c2-535b1131744a.png">
         <img width="250" alt="Made with love by Builder.io" src="https://user-images.githubusercontent.com/844291/230786555-a58479e4-75f3-4222-a6eb-74c5af953eac.png">
       </picture>
   </a>
</p>
