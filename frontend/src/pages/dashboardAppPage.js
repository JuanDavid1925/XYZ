import { Helmet } from 'react-helmet-async';
import { faker } from '@faker-js/faker';
// @mui
import { useTheme } from '@mui/material/styles';
import { Grid, Container, Typography } from '@mui/material';
// components
import Iconify from '../components/iconify';
import {
  AppWebsiteVisits,
  AppWidgetSummary,
  AppConversionRates,

} from '../sections/@dashboard/app';

export default function DashboardAppPage() {
  const theme = useTheme();

  return (
    <>


      <Container maxWidth="xl">
        <Typography variant="h4" sx={{ mb: 5 }}>
          Hola, Bienvenido
        </Typography>

        <Grid container spacing={3}>
          <Grid item xs={12} sm={6} md={3}>
            <AppWidgetSummary title="Hoteles consultados" total={14} icon={'ant-design:android-filled'} />
          </Grid>

          <Grid item xs={12} sm={6} md={3}>
            <AppWidgetSummary title="Habitaciones presentadas" total={135} color="info" icon={'ant-design:apple-filled'} />
          </Grid>

          <Grid item xs={12} sm={6} md={3}>
            <AppWidgetSummary title="Clientes satisfechos" total={1723} color="warning" icon={'ant-design:windows-filled'} />
          </Grid>

          <Grid item xs={12} md={6} lg={8}>
            <AppWebsiteVisits
              title="Hoteles más consultados"
              subheader="En los últimos meses"
              chartLabels={[
                '01/01/2003',
                '02/01/2003',
                '03/01/2003',
                '04/01/2003',
                '05/01/2003',
                '06/01/2003',
                '07/01/2003',
                '08/01/2003',
                '09/01/2003',
                '10/01/2003',
                '11/01/2003',
              ]}
              chartData={[
                {
                  name: 'Atlantis The Palm',
                  type: 'column',
                  fill: 'solid',
                  data: [23, 11, 22, 27, 13, 22, 37, 21, 44, 22, 30],
                },
                {
                  name: 'The Plaza Hotel',
                  type: 'area',
                  fill: 'gradient',
                  data: [44, 55, 41, 67, 22, 43, 21, 41, 56, 27, 43],
                },
                {
                  name: 'The Ritz-Carlton',
                  type: 'line',
                  fill: 'solid',
                  data: [30, 25, 36, 30, 45, 35, 64, 52, 59, 36, 39],
                },
              ]}
            />
          </Grid>

          <Grid item xs={12} md={6} lg={8}>
            <AppConversionRates
              title="Hoteles consultados"
              chartData={[
                { label: 'Burj Al Arab', value: 400 },
                { label: 'The Peninsula ', value: 430 },
                { label: 'Taj Mahal Palace', value: 448 },
                { label: 'The Waldorf Astoria ', value: 470 },
                { label: 'The Savoy ', value: 540 },
                { label: 'Marina Bay Sands ', value: 580 },
                { label: 'Hotel Ritz', value: 690 },
                { label: 'The Ritz-Carlton ', value: 1100 },
                { label: 'The Plaza Hotel', value: 1200 },
                { label: 'Atlantis The Palm', value: 1380 },
              ]}
            />
          </Grid>








        </Grid>
      </Container>
    </>
  );
}