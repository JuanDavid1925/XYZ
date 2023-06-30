import { Landing_page, SignIn, SignUp } from "./pages";
import DashboardLayout from "./widgets/layout/dashboard"
import UserPage from "./pages/userPage";
import DashboardAppPage from "./pages/dashboardAppPage";
import DashboardUser from "./pages/dashboardUser";
import {
  HomeIcon,
  ArrowRightOnRectangleIcon,
  UserPlusIcon,
} from "@heroicons/react/24/solid";
import { useRoutes, Navigate } from "react-router-dom";

export default function Router() {
  const routes = useRoutes([
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
      name: "dashboard user",
      path: "/dashboard/user",
      element: <DashboardUser />,
    },
    {
      icon: UserPlusIcon,
      name: "Dashboard Admin",
      path: "/dashboard/admin",
      element: <DashboardLayout />,
      children: [
        { element: <Navigate to="/dashboard/admin/app" />, index: true },
        { path: 'app', element: <DashboardAppPage /> },
        { path: 'user', element: <UserPage /> },

      ],
    },
    {
      path: '*',
      element: <Navigate to="/home" replace />,
    },
  ]);
  return routes;
}