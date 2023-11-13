import Head from "next/head";
import Navbar from "@/components/Navbar";
import Card from "@/components/Card";

import "../app/globals.css";
export default function Home({ hotels }) {
  return (
    <div>
      <Head>
        <title> Airbnb Clone </title>
      </Head>
      <Navbar></Navbar>

      {/* Cards */}
      <div className="mx-5 my-7">
        <h1 className="text-3xl font-semibold mb-3">Properties</h1>
        <section className="flex">
          {hotels.map((hotel) => {
            return <Card key={hotel.id} props={hotel} />;
          })}
        </section>
      </div>
    </div>
  );
}

export async function getStaticProps() {
  const res = await fetch("http://localhost:8000/api/properties/");
  const hotels = await res.json();

  return {
    props: { hotels },
  };
}
