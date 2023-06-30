import { Select, Option } from "@material-tailwind/react";
// @mui
import { Grid } from '@mui/material';
import {
  Card,
  CardHeader,
  CardBody,
  Typography,
  Button,
  CardFooter,
} from "@material-tailwind/react";


export default function DashboardUser() {
  return (
    <div className="mt-10 ml-20">
      <Typography variant="h3" sx={{ mb: 5 }} >
        Hola, bienvenid@
      </Typography>
      <div className="w-72 mt-20 ">
        <Select
          label="Cali"
          animate={{
            mount: { y: 0 },
            unmount: { y: 25 },
          }}
        >
          <Option>Cali</Option>
          <Option>Bogotá</Option>
          <Option>Medellín</Option>
          <Option>Cartagena</Option>
          <Option>San Andrés</Option>
          <Option>Madrid</Option>
          <Option>París</Option>
          <Option>Dubai</Option>
          <Option>Venecia</Option>
          <Option>Londres</Option>
        </Select>
      </div>



      <Grid container spacing={5}>
        <Grid item xs={12} sm={6} md={3}>
          <Card className="w-66">
            <CardHeader shadow={false} floated={false} className="h-96">
              <img
                src="https://cf.bstatic.com/xdata/images/hotel/square200/64120960.jpg?k=45bb7ab0f44f4b55567f20b7595a33cb2f7aec590bbe8bb3abb290a3cc4d6b44&o="
                className="w-full h-full object-cover"
              />
            </CardHeader>
            <CardBody>
              <div className="flex items-center justify-between mb-2">
                <Typography color="blue-gray" className="font-medium">
                  Hotel Dann Cali
                </Typography>
                <Typography color="blue-gray" className="font-medium">
                  $304.000
                </Typography>
              </div>
              <Typography variant="small" color="gray" className="font-normal opacity-75">
                Habitación Doble
              </Typography>
            </CardBody>
            <CardFooter className="pt-0">
              <a href="https://www.hotelesdanncali.com/">
                <Button
                  ripple={false}
                  fullWidth={true}
                  className="bg-blue-gray-900/10 text-blue-gray-900 shadow-none hover:shadow-none hover:scale-105 focus:shadow-none focus:scale-105 active:scale-100"

                >
                  Página principal
                </Button>
              </a>


            </CardFooter>
          </Card>
        </Grid>




        <Grid item xs={12} sm={6} md={3}>
          <Card className="w-66">
            <CardHeader shadow={false} floated={false} className="h-96">
              <img
                src="https://cf.bstatic.com/xdata/images/hotel/square200/441812075.jpg?k=31a2a88656335970658e5e96cffd1f94baa5368baa245236640c7c91ac4d0eee&o="
                className="w-full h-full object-cover"
              />
            </CardHeader>
            <CardBody>
              <div className="flex items-center justify-between mb-2">
                <Typography color="blue-gray" className="font-medium">
                  Hotel Spiwak Spirito
                </Typography>
                <Typography color="blue-gray" className="font-medium">
                  $285.000
                </Typography>
              </div>
              <Typography variant="small" color="gray" className="font-normal opacity-75">
                Habitación Doble - 2 camas dobles              </Typography>
            </CardBody>
            <CardFooter className="pt-0">
              <a href="https://spiwak.com/">
                <Button
                  ripple={false}
                  fullWidth={true}
                  className="bg-blue-gray-900/10 text-blue-gray-900 shadow-none hover:shadow-none hover:scale-105 focus:shadow-none focus:scale-105 active:scale-100"

                >
                  Página principal
                </Button>
              </a>
            </CardFooter>
          </Card>
        </Grid>



        <Grid item xs={12} sm={6} md={3}>
          <Card className="w-66">
            <CardHeader shadow={false} floated={false} className="h-96">
              <img
                src="https://cf.bstatic.com/xdata/images/hotel/square200/4148718.jpg?k=fdeca134a326c9632feea9fe509399d6bd2e2967428e7299a29b494f4b7f0273&o="
                className="w-full h-full object-cover"
              />
            </CardHeader>
            <CardBody>
              <div className="flex items-center justify-between mb-2">
                <Typography color="blue-gray" className="font-medium">
                  Now Hotel
                </Typography>
                <Typography color="blue-gray" className="font-medium">
                  $260.000
                </Typography>
              </div>
              <Typography variant="small" color="gray" className="font-normal opacity-75">
                Suite Estándar              </Typography>
            </CardBody>
            <CardFooter className="pt-0">
              <a href="https://nowhotel.com.co/">
                <Button
                  ripple={false}
                  fullWidth={true}
                  className="bg-blue-gray-900/10 text-blue-gray-900 shadow-none hover:shadow-none hover:scale-105 focus:shadow-none focus:scale-105 active:scale-100"

                >
                  Página principal
                </Button>
              </a>
            </CardFooter>
          </Card>
        </Grid>


        <Grid item xs={12} sm={6} md={3}>
          <Card className="w-66">
            <CardHeader shadow={false} floated={false} className="h-96">
              <img
                src="https://cf.bstatic.com/xdata/images/hotel/square200/410434169.jpg?k=85685026ce3a09b198fbd1a347126270422a0331a8d62780180a05e9f89386cb&o="
                className="w-full h-full object-cover"
              />
            </CardHeader>
            <CardBody>
              <div className="flex items-center justify-between mb-2">
                <Typography color="blue-gray" className="font-medium">
                  Hotel Intercontinental Cali, an IHG Hotel
                </Typography>
                <Typography color="blue-gray" className="font-medium">
                  $423.920
                </Typography>
              </div>
              <Typography variant="small" color="gray" className="font-normal opacity-75">
                Habitación Estándar              </Typography>
            </CardBody>
            <CardFooter className="pt-0">
              <a href="https://www.hotelesestelar.com/es/hotel/intercontinental-cali">
                <Button
                  ripple={false}
                  fullWidth={true}
                  className="bg-blue-gray-900/10 text-blue-gray-900 shadow-none hover:shadow-none hover:scale-105 focus:shadow-none focus:scale-105 active:scale-100"

                >
                  Página principal
                </Button>
              </a>
            </CardFooter>
          </Card>
        </Grid>


        <Grid item xs={12} sm={6} md={3}>
          <Card className="w-66">
            <CardHeader shadow={false} floated={false} className="h-96">
              <img
                src="https://cf.bstatic.com/xdata/images/hotel/square200/240980580.jpg?k=484ee8ce4ef893245ce9c3c17f0f614ee03c6647810f6917c07cce66a14cc018&o="
                className="w-full h-full object-cover"
              />
            </CardHeader>
            <CardBody>
              <div className="flex items-center justify-between mb-2">
                <Typography color="blue-gray" className="font-medium">
                  Alko Hotel Casa Nispero
                </Typography>
                <Typography color="blue-gray" className="font-medium">
                  $612.000
                </Typography>
              </div>
              <Typography variant="small" color="gray" className="font-normal opacity-75">
                Habitación Doble              </Typography>
            </CardBody>
            <CardFooter className="pt-0">
              <a href="https://www.alkohoteles.com/es/hotel-alko-hotel-casa-nispero-en-cali/">
                <Button
                  ripple={false}
                  fullWidth={true}
                  className="bg-blue-gray-900/10 text-blue-gray-900 shadow-none hover:shadow-none hover:scale-105 focus:shadow-none focus:scale-105 active:scale-100"

                >
                  Página principal
                </Button>
              </a>
            </CardFooter>
          </Card>
        </Grid>

      </Grid>
    </div>
  )
};
