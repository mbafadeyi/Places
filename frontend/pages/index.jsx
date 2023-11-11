import Head from "next/head";
import Navbar from "@/components/Navbar";

import "../app/globals.css";
export default function Home() {
  return (
    <div>
      <Head>
        <title> Airbnb Clone </title>
      </Head>
      <Navbar></Navbar>
    </div>
  );
}
