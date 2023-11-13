/** @type {import('next').NextConfig} */
const nextConfig = {
  images: {
    domains: ["media.gettyimages.com"],
  },
  // images: {
  //   remotePatterns: [
  //     {
  //       protocol: "https",
  //       hostname: "res.cloudinary.com",
  //       // hostname: "localhost:8000",
  //       pathname: "**",
  //     },
  //   ],
  // },
};

module.exports = nextConfig;
