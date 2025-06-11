<template>
  <!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <link rel="stylesheet" href="style.css">
  <title>Tableau de bord - Réservations</title>
  
</head>
<body>
  <div class="container">
    <nav>
      <h2>Hôtel Admin</h2>
      <router-link to="/">Dashboard</router-link>
      <router-link to="/chambres">Chambres</router-link>
      <router-link to="/reservations">Réservations</router-link>
      
    </nav>
    <main>
      <header>
        <h1>Tableau de bord</h1>
        
      </header>

      
  <section class="stats">
    <div class="card">
      <h3>Chambres Occupées</h3>
      <p id="chambres_occupees">{{ chambres_occupees }} / {{ total_chambres }}</p>
    </div>
    <div class="card">
      <h3>Disponibles</h3>
      <p id="chambres_disponibles">{{ chambres_disponibles }}</p>
    </div>
    <div class="card">
      <h3>Réservations en attente</h3>
      <p id="reservations_encours">{{ reservations_encours }}/{{ total_reservation }}</p>
    </div>
  </section>


      <section class="reservations">
        <h2>Réservations récentes</h2>
        <table>
          <thead>
            <tr>
              <th>Client</th>
              <th>Chambre</th>
              <th>Date</th>
              <th>Statut</th>
            </tr>
          </thead>
          <tbody>
      <tr v-for="reservation in reservations.slice(0, 5)" :key="reservation.id">
        <td>{{ reservation.chambre.numero }}</td>
              <td>{{ reservation.client_nom }}</td>
              <td>{{ reservation.client_contact }}</td>
              <td>{{ reservation.date_debut }} - {{ reservation.date_fin }}</td>
              <td>{{ reservation.statut }}</td>
      </tr>
    </tbody>
        </table>
      </section>
    </main>
  </div>
</body>
</html>

</template>

<script setup>
const reservations = ref([])

const fetchReservations = async () => {
  try {
    const res = await axios.get("http://localhost:8000/api/reservations/?ordering=-date_creation")
    reservations.value = res.data
  } catch (error) {
    console.error("Erreur lors du chargement des réservations :", error)
  }
}


fetch("http://localhost:8000/api/dashboard/")
    .then(response => response.json())
    .then(data => {
      document.getElementById("chambres_occupees").innerText = `${data.chambres_occupees} / ${data.total_chambres}`;
      document.getElementById("chambres_disponibles").innerText = data.chambres_disponibles;
      document.getElementById("reservations_encours").innerText = `${data.reservations_encours} / ${data.total_reservation}`;
    })
    .catch(error => {
      console.error("Erreur lors du chargement des données du tableau de bord :", error);
    });

    setInterval(() => {
  fetch("http://localhost:8000/api/dashboard/")
    .then(res => res.json())
    .then(data => {
      document.getElementById("chambres_occupees").innerText = `${data.chambres_occupees} / ${data.total_chambres}`;
      document.getElementById("chambres_disponibles").innerText = data.chambres_disponibles;
      document.getElementById("reservations_encours").innerText = `${data.reservations_encours} / ${data.total_reservation}`;
    });
}, 3000); // toutes les 30 secondes


import { ref, onMounted } from 'vue'
import axios from 'axios'

const total_chambres = ref(0)
const chambres_occupees = ref(0)
const chambres_disponibles = ref(0)
const reservations_encours = ref(0)

const fetchDashboardData = async () => {
  try {
    const response = await axios.get('http://localhost:8000/api/dashboard/')
    total_chambres.value = response.data.total_chambres
    chambres_occupees.value = response.data.chambres_occupees
    chambres_disponibles.value = response.data.chambres_disponibles
    reservations_encours.value = response.data.reservations_encours
  } catch (error) {
    console.error('Erreur lors du chargement du tableau de bord :', error)
  }
}

onMounted(() => {
  fetchDashboardData()
  fetchReservations()
  setInterval(() => {
    fetchDashboardData()
    fetchReservations()
  }, 30000)
})

</script>

<style >
@import '../assets/style.css';
</style>
