import { Link } from "react-router-dom";
import {
  Card,
  CardHeader,
  CardBody,
  CardFooter,
  Input,
  Checkbox,
  Button,
  Typography,
} from "@material-tailwind/react";
import { SimpleFooter } from "../widgets/layout";

export function SignUp() {
  return (
    <>
      <img
        alt='Registro'
        src="/inicio y registro.jpg"
        className="absolute inset-0 z-0 h-full w-full object-cover"
      />
      <div className="absolute inset-0 z-0 h-full w-full bg-black/50" />
      <div className="container mx-auto p-4">
        <Card className="absolute top-2/4 left-2/4 w-full max-w-[24rem] -translate-y-2/4 -translate-x-2/4">
          <CardHeader
            variant="gradient"
            color="blue"
            className="mb-4 grid h-28 place-items-center"
          >
            <Typography variant="h3" color="white">
              Registrarse
            </Typography>
          </CardHeader>
          <CardBody className="flex flex-col gap-4">
            <Input variant="standard" label="Correo electrónico" size="lg" />
            <Input variant="standard" type="password" label="Contraseña" size="lg" />
            <Input
              variant="standard"
              type="password"
              label="Confirmar contraseña"
              size="lg"
            />
            <div className="-ml-2.5">
              <Checkbox label="Acepto terminos y condiciones" />
            </div>
          </CardBody>
          <CardFooter className="pt-0">
            <Button variant="gradient" fullWidth>
              Registrarse
            </Button>
            <button className="flex flex-wrap justify-center w-full border border-gray-300 hover:border-gray-500 px-2 py-1.5 rounded-md">
              <img className="w-5 mr-2"
                alt="Google"
                src="https://lh3.googleusercontent.com/COxitqgJr1sJnIDe8-jiKhxDx1FrYbtRHKJ9z_hELisAlapwE9LUPh6fcXIfb5vwpbMl4xl9H9TRFPc5NOO8Sb3VSgIBrfRYvW6cUA" />
              Registrarse con Google
            </button>
            <button className="flex flex-wrap justify-center w-full border border-gray-300 hover:border-gray-500 px-2 py-1.5 rounded-md">
              <img className="w-5 mr-2"
                alt="facebook"
                src="https://www.facebook.com/images/fb_icon_325x325.png" />
              Registrarse con Facebook
            </button>
            <Typography variant="small" className="mt-6 flex justify-center">
              Ya tienes una cuenta?
              <Link to="/sign-in">
                <Typography
                  as="span"
                  variant="small"
                  color="blue"
                  className="ml-1 font-bold"
                >
                  Inicia sesión
                </Typography>
              </Link>
            </Typography>
          </CardFooter>
        </Card>
      </div>
      <div className="container absolute bottom-6 left-2/4 z-10 mx-auto -translate-x-2/4 text-white">
        <SimpleFooter />
      </div>
    </>
  );
}

export default SignUp;