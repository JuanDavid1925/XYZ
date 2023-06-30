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
        Hola, Bienvenido
      </Typography>
      <div className="w-72 mt-20 ">
        <Select
          label="Selecciona una ciudad"
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
          <Card className="w-96">
            <CardHeader shadow={false} floated={false} className="h-96">
              <img
                src="https://images.unsplash.com/photo-1629367494173-c78a56567877?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=927&q=80"
                className="w-full h-full object-cover"
              />
            </CardHeader>
            <CardBody>
              <div className="flex items-center justify-between mb-2">
                <Typography color="blue-gray" className="font-medium">
                  Apple AirPods
                </Typography>
                <Typography color="blue-gray" className="font-medium">
                  $95.00
                </Typography>
                <Typography color="blue-gray" className="font-medium">
                  $95.00
                </Typography>
                <Typography color="blue-gray" className="font-medium">
                  $95.00
                </Typography>
              </div>
              <Typography variant="small" color="gray" className="font-normal opacity-75">
                With plenty of talk and listen time, voice-activated Siri access, and an available wireless charging case.
              </Typography>
            </CardBody>
            <CardFooter className="pt-0">
              <Button
                ripple={false}
                fullWidth={true}
                className="bg-blue-gray-900/10 text-blue-gray-900 shadow-none hover:shadow-none hover:scale-105 focus:shadow-none focus:scale-105 active:scale-100"
              >
                Add to Cart
              </Button>
            </CardFooter>
          </Card>
        </Grid>




        <Grid item xs={12} sm={6} md={3}>
          <Card className="w-96">
            <CardHeader shadow={false} floated={false} className="h-96">
              <img
                src="https://images.unsplash.com/photo-1629367494173-c78a56567877?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=927&q=80"
                className="w-full h-full object-cover"
              />
            </CardHeader>
            <CardBody>
              <div className="flex items-center justify-between mb-2">
                <Typography color="blue-gray" className="font-medium">
                  Apple AirPods
                </Typography>
                <Typography color="blue-gray" className="font-medium">
                  $95.00
                </Typography>
              </div>
              <Typography variant="small" color="gray" className="font-normal opacity-75">
                With plenty of talk and listen time, voice-activated Siri access, and an available wireless charging case.
              </Typography>
            </CardBody>
            <CardFooter className="pt-0">
              <Button
                ripple={false}
                fullWidth={true}
                className="bg-blue-gray-900/10 text-blue-gray-900 shadow-none hover:shadow-none hover:scale-105 focus:shadow-none focus:scale-105 active:scale-100"
              >
                Add to Cart
              </Button>
            </CardFooter>
          </Card>
        </Grid>



        <Grid item xs={12} sm={6} md={3}>
          <Card className="w-96">
            <CardHeader shadow={false} floated={false} className="h-96">
              <img
                src="https://images.unsplash.com/photo-1629367494173-c78a56567877?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=927&q=80"
                className="w-full h-full object-cover"
              />
            </CardHeader>
            <CardBody>
              <div className="flex items-center justify-between mb-2">
                <Typography color="blue-gray" className="font-medium">
                  Apple AirPods
                </Typography>
                <Typography color="blue-gray" className="font-medium">
                  $95.00
                </Typography>
              </div>
              <Typography variant="small" color="gray" className="font-normal opacity-75">
                With plenty of talk and listen time, voice-activated Siri access, and an available wireless charging case.
              </Typography>
            </CardBody>
            <CardFooter className="pt-0">
              <Button
                ripple={false}
                fullWidth={true}
                className="bg-blue-gray-900/10 text-blue-gray-900 shadow-none hover:shadow-none hover:scale-105 focus:shadow-none focus:scale-105 active:scale-100"
              >
                Add to Cart
              </Button>
            </CardFooter>
          </Card>
        </Grid>


        <Grid item xs={12} sm={6} md={3}>
          <Card className="w-96">
            <CardHeader shadow={false} floated={false} className="h-96">
              <img
                src="https://images.unsplash.com/photo-1629367494173-c78a56567877?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=927&q=80"
                className="w-full h-full object-cover"
              />
            </CardHeader>
            <CardBody>
              <div className="flex items-center justify-between mb-2">
                <Typography color="blue-gray" className="font-medium">
                  Apple AirPods
                </Typography>
                <Typography color="blue-gray" className="font-medium">
                  $95.00
                </Typography>
              </div>
              <Typography variant="small" color="gray" className="font-normal opacity-75">
                With plenty of talk and listen time, voice-activated Siri access, and an available wireless charging case.
              </Typography>
            </CardBody>
            <CardFooter className="pt-0">
              <Button
                ripple={false}
                fullWidth={true}
                className="bg-blue-gray-900/10 text-blue-gray-900 shadow-none hover:shadow-none hover:scale-105 focus:shadow-none focus:scale-105 active:scale-100"
              >
                Add to Cart
              </Button>
            </CardFooter>
          </Card>
        </Grid>


        <Grid item xs={12} sm={6} md={3}>
          <Card className="w-96">
            <CardHeader shadow={false} floated={false} className="h-96">
              <img
                src="https://images.unsplash.com/photo-1629367494173-c78a56567877?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=927&q=80"
                className="w-full h-full object-cover"
              />
            </CardHeader>
            <CardBody>
              <div className="flex items-center justify-between mb-2">
                <Typography color="blue-gray" className="font-medium">
                  Apple AirPods
                </Typography>
                <Typography color="blue-gray" className="font-medium">
                  $95.00
                </Typography>
              </div>
              <Typography variant="small" color="gray" className="font-normal opacity-75">
                With plenty of talk and listen time, voice-activated Siri access, and an available wireless charging case.
              </Typography>
            </CardBody>
            <CardFooter className="pt-0">
              <Button
                ripple={false}
                fullWidth={true}
                className="bg-blue-gray-900/10 text-blue-gray-900 shadow-none hover:shadow-none hover:scale-105 focus:shadow-none focus:scale-105 active:scale-100"
              >
                Add to Cart
              </Button>
            </CardFooter>
          </Card>
        </Grid>

        <Grid item xs={12} sm={6} md={3}>
          <Card className="w-96">
            <CardHeader shadow={false} floated={false} className="h-96">
              <img
                src="https://images.unsplash.com/photo-1629367494173-c78a56567877?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=927&q=80"
                className="w-full h-full object-cover"
              />
            </CardHeader>
            <CardBody>
              <div className="flex items-center justify-between mb-2">
                <Typography color="blue-gray" className="font-medium">
                  Apple AirPods
                </Typography>
                <Typography color="blue-gray" className="font-medium">
                  $95.00
                </Typography>
              </div>
              <Typography variant="small" color="gray" className="font-normal opacity-75">
                With plenty of talk and listen time, voice-activated Siri access, and an available wireless charging case.
              </Typography>
            </CardBody>
            <CardFooter className="pt-0">
              <Button
                ripple={false}
                fullWidth={true}
                className="bg-blue-gray-900/10 text-blue-gray-900 shadow-none hover:shadow-none hover:scale-105 focus:shadow-none focus:scale-105 active:scale-100"
              >
                Add to Cart
              </Button>
            </CardFooter>
          </Card>
        </Grid>

      </Grid>
    </div>
  )
};