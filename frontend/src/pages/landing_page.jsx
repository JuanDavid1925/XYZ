import React from "react";
import {
  Card,
  CardBody,
  CardHeader,
  Typography,
} from "@material-tailwind/react";
import { UsersIcon } from "@heroicons/react/24/solid";
import { PageTitle, Footer } from "../widgets/layout";
import { FeatureCard, TeamCard } from "../widgets/cards";
import { featuresData, teamData } from "../data";
import News from "../components/news";

export function Landing_page() {
  return (
    <>
      <div className="relative flex h-screen content-center items-center justify-center pt-16 pb-32">
        <div className="absolute top-0 h-full w-full bg-[url('https://images.unsplash.com/photo-1511895426328-dc8714191300?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1170&q=80')] bg-cover bg-center" />
        <div className="absolute top-0 h-full w-full bg-black/50 bg-cover bg-center" />
        <div className="max-w-8xl container relative mx-auto">
          <div className="flex flex-wrap items-center">
            <div className="ml-auto mr-auto w-full px-4 text-center lg:w-8/12">
              <Typography
                variant="h1"
                color="white"
                className="mb-6 font-black"
              >
                Tu viaje empieza con nosotros.
              </Typography>
              <Typography variant="lead" color="white" className="opacity-80">
                Ya sea que estés buscando un hotel para tus vacaciones, un viaje de negocios o una escapada de fin de semana,
                en nosotros encontrarás a tu compañero ideal.
              </Typography>
            </div>
          </div>
        </div>
      </div>
      <section className="-mt-32 bg-gray-50 px-4 pb-20 pt-4">
        <div className="container mx-auto">
          <div className="grid grid-cols-1 gap-6 md:grid-cols-2 lg:grid-cols-3">
            {featuresData.map(({ color, title, icon, description }) => (
              <FeatureCard
                key={title}
                color={color}
                title={title}
                icon={React.createElement(icon, {
                  className: "w-5 h-5 text-white",
                })}
                description={description}
              />
            ))}
          </div>
          <div className="mt-32 flex flex-wrap items-center">
            <div className="mx-auto -mt-8 w-full px-4 md:w-5/12">
              <div className="mb-6 inline-flex h-16 w-16 items-center justify-center rounded-full bg-white p-3 text-center shadow-lg">
                <UsersIcon className="h-6 w-6 text-blue-gray-900" />
              </div>
              <Typography
                variant="h3"
                className="mb-3 font-bold"
                color="blue-gray"
              >
                Recomendaciones personalizadas
              </Typography>
              <Typography className="mb-8 font-normal text-blue-gray-500">
                En base a tus preferencias y actividades anteriores,
                te ofrecemos recomendaciones personalizadas utilizando algoritmos inteligentes.
                Podemos sugerirte hoteles similares a los que has reservado previamente, restaurantes populares en tu destino o atracciones turísticas que podrían interesarte.
                Estas recomendaciones te ayudarán a descubrir nuevos lugares y experiencias.
                <br />

              </Typography>

            </div>
            <div className="mx-auto mt-24 flex w-full justify-center px-4 md:w-4/12 lg:mt-0">
              <Card className="shadow-lg shadow-gray-500/10">
                <CardHeader className="relative h-56">
                  <img
                    alt="info_ia"
                    src='./ia.jpg'
                    className="h-full w-full"
                  />
                </CardHeader>
                <CardBody>
                  <Typography
                    variant="h5"
                    color="blue-gray"
                    className="mb-3 font-bold"
                  >
                    Análisis desde diferentes enfoques
                  </Typography>
                  <Typography className="font-normal text-blue-gray-500">
                    Nos basamos en el análisis de las preferencias de los usuarios y la búsqueda de patrones similares en otros usuarios para ofrecer recomendaciones relevantes.
                  </Typography>
                </CardBody>
              </Card>
            </div>
          </div>
        </div>
      </section>
      <section className="px-4 pt-20 pb-48">
        <div className="container mx-auto">
          <PageTitle heading="Planifica tu viaje con nosotros.">
            Somos una compañia diseñada para ayudarte a encontrar información sobre hoteles y habitaciones, así como para planificar y organizar tus viajes de manera eficiente.
          </PageTitle>
          <div className="mt-24 grid grid-cols-1 gap-12 gap-x-24 md:grid-cols-2 xl:grid-cols-4">
            {teamData.map(({ img }) => (
              <TeamCard
                name=''
                img={img}
              />
            ))}
          </div>
        </div>
      </section>
      <section className="relative bg-blue-gray-50/50 py-24 px-4">
        <div className="container mx-auto">
          <PageTitle heading="Entérate de las últimas novedades.">
            Contamos con una sección de noticias para que estés enterado de las últimas ofertas y no te pierdas la oportunidad de tener tu viaje soñado.
          </PageTitle>
          <div className="mx-auto mt-10 mb-48">

            <News />

          </div>
        </div>
      </section>
      <div className="bg-blue-gray-50/50">
        <Footer />
      </div>
    </>
  );
}

export default Landing_page;