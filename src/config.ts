export const SITE = {
  website: "https://www.yunchujiao.com/", // replace this with your deployed domain
  author: "云触角（重庆）科技有限公司",
  profile: "https://www.yunchujiao.com/",
  desc: "云触角科技 - 您身边的IT服务专家，提供IT运维、电脑维修、系统安装、网站建设等服务。",
  title: "云触角（重庆）科技有限公司",
  ogImage: "yunchujiao-og.jpg",
  lightAndDarkMode: true,
  postPerIndex: 3,
  postPerPage: 6,
  scheduledPostMargin: 15 * 60 * 1000, // 15 minutes
  showArchives: true,
  showBackButton: true, // show back button in post detail
  editPost: {
    enabled: false,
    text: "",
    url: "",
  },
  dynamicOgImage: true,
  dir: "ltr", // "rtl" | "auto"
  lang: "zh-cn", // html lang code. Set this empty and default will be "en"
  timezone: "Asia/Shanghai", // Default global timezone (IANA format)
} as const;
