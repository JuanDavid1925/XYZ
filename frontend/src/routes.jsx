import { Landing_page, SignIn, SignUp, UserPage } from "./pages";
import DashboardLayout from "./widgets/layout/dashboard"
import {
  HomeIcon,
  ArrowRightOnRectangleIcon,
  UserPlusIcon,
} from "@heroicons/react/24/solid";

export const routes = [
  {
    icon: HomeIcon,
    name: "home",
    path: "/home",
    element: <Landing_page />,
  },
  {
    icon: ArrowRightOnRectangleIcon,
    name: "Sign In",
    path: "/sign-in",
    element: <SignIn />,
  },
  {
    icon: UserPlusIcon,
    name: "Sign Up",
    path: "/sign-up",
    element: <SignUp />,
  },
  {
    icon: UserPlusIcon,
    name: "Dashboard Admin",
    path: "/Dashboard/Admin",
    element: <DashboardLayout />,
  },
  {
    icon: UserPlusIcon,
    name: "user list",
    path: "/dashboard/user",
    element: <UserPage />,
  },
];

export default routes;