// component
import SvgColor from '../../../../components/svg-color';

// ----------------------------------------------------------------------

const icon = (name) => <SvgColor src={`/navbar/${name}.svg`} sx={{ width: 1, height: 1 }} />;

const navConfig = [
  {
    title: 'Inicio',
    path: '/dashboard/app',
    icon: icon('ic_analytics'),
  },
  {
    title: 'Usuarios',
    path: '/dashboard/admin/user',
    icon: icon('ic_user'),
  },
  {
    title: 'Noticias',
    path: '/dashboard/noticias',
    icon: icon('ic_blog'),
  },
  {
    title: 'Reportes',
    path: '/dashboard/reportes',
    icon: icon('ic_cart'),
  },
];

export default navConfig;