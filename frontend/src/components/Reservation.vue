<template>
    

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
        <h1>Réservations</h1>
        
        <button class="btn" @click="ouvrirFormulaire()">+ Nouvelle réservation</button>
      </header>

      <section class="section">
        <h2>Réservations en cours</h2>
        <table>
          <thead>
            <tr>
              <th>Chambre</th>
              <th>Client</th>
              <th>Contact</th>
              <th>Dates début - fin</th>
              <th>Statut</th>
              <th>Actions</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="reservation in reservations" :key="reservation.id">
              
              <td>{{ reservation.chambre.numero }}</td>
              <td>{{ reservation.client_nom }}</td>
              <td>{{ reservation.client_contact }}</td>
              <td>{{ reservation.date_debut }} - {{ reservation.date_fin }}</td>
              <td>{{ reservation.statut }}</td>
              <td class="actions">
                <button class="btn" @click="modifierReservation(reservation)">Modifier</button>
                <button class="btn btn-secondary" @click="annulerReservation(reservation)">Annuler</button>
              </td>
            </tr>
            
          </tbody>
        </table>
      </section>

      <section class="section" v-if="formVisible">
        <h2>Créer une réservation</h2>
        <form @submit.prevent="submitReservation">
        <input v-model="form.client_nom" type="text" placeholder="Nom du client" required />
        <input v-model="form.client_contact" type="text" placeholder="Contact du client" required />

        <select v-model="form.chambre_id" required>
          <option disabled value="">-- Chambre --</option>
          <option v-for="chambre in chambres" :key="chambre.id" :value="chambre.id">
            {{ chambre.numero }} ({{ chambre.type }})
          </option>
        </select>

        <input v-model="form.date_debut" type="date" required />
        <input v-model="form.date_fin" type="date" required />

        <select v-model="form.statut" required>
  <option disabled value="">-- Statut --</option>
  <option value="EN_ATTENTE">EN_ATTENTE</option>
  <option value="CONFIRMEE">CONFIRMEE</option>
  <option value="ANNULEE">ANNULEE</option>
</select>




        <button type="submit" class="btn">
        {{ isEditing ? 'Modifier la réservation' : 'Réserver' }}
        </button>

        <button class="btn btn-secondary" type="button" @click="annuler()">Annuler</button>
        </form>
      </section>
    </main>
  </div>
</body>



</template>

<script>
import axios from 'axios'

export default {
  data() {
  return {
    reservations: [],
    chambres: [],
    statuts: ["EN_ATTENTE", "CONFIRMEE", "ANNULEE"],
    form: {
      client_nom: '',
      client_contact: '',
      chambre_id: '',
      date_debut: '',
      date_fin: '',
      statut: ''
    },
    formVisible: false,
    isEditing: false,
    editReservationId: null,
  };
}
,
  methods: {
    modifierReservation(reservation) {
      this.form = {
        client_nom: reservation.client_nom,
        client_contact: reservation.client_contact,
        chambre_id: reservation.chambre.id,
        date_debut: reservation.date_debut,
        date_fin: reservation.date_fin,
        statut: reservation.statut
      };
      this.formVisible = true;
      this.isEditing = true;
      this.editReservationId = reservation.id;
    },

    annulerReservation(reservation) {
      fetch(`http://localhost:8000/api/reservations/${reservation.id}/`, {
        method: 'DELETE'
      })
        .then(() => this.fetchReservations())
        .catch(err => console.error("Erreur suppression :", err));
    },

    ouvrirFormulaire() {
  this.form = {
    client_nom: '',
    client_contact: '',
    chambre_id: '',
    date_debut: '',
    date_fin: '',
    statut: 'EN_ATTENTE' // ← Ajout d'une valeur valide
  };
  this.formVisible = true;
  this.isEditing = false;
  this.editReservationId = null;
},

    submitReservation() {
  console.log("Formulaire soumis avec : ", this.form); // AJOUT
  const payload = {
    client_nom: this.form.client_nom,
    client_contact: this.form.client_contact,
    chambre: this.form.chambre_id,
    date_debut: this.form.date_debut,
    date_fin: this.form.date_fin,
    statut: this.form.statut
  };

  const url = this.isEditing
    ? `http://localhost:8000/api/reservations/${this.editReservationId}/`
    : "http://localhost:8000/api/reservations/";

  const method = this.isEditing ? "PUT" : "POST";

  fetch(url, {
    method,
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload)
  })
    .then(res => {
      if (!res.ok) throw new Error("Échec de l'enregistrement");
      return res.json();
    })
    .then(() => {
      this.resetForm();
      this.fetchReservations();
    })
    .catch(err => {
      console.error("Erreur lors de l’envoi :", err);
    });
},


    annuler() {
      this.formVisible = false;
      this.resetForm();
    },

    resetForm() {
  this.form = {
    client_nom: '',
    client_contact: '',
    chambre_id: '',
    date_debut: '',
    date_fin: '',
    statut: 'EN_ATTENTE' // ← Idem ici
  };
  this.isEditing = false;
  this.editReservationId = null;
},


    fetchReservations() {
      fetch("http://localhost:8000/api/reservations/")
        .then(res => res.json())
        .then(data => {
          this.reservations = data;
        });
    },
  },

  mounted() {
    axios.get('http://127.0.0.1:8000/api/reservations/')
      .then(response => {
        this.reservations = response.data;
      });

    axios.get('http://127.0.0.1:8000/api/chambres/')
      .then(response => {
        this.chambres = response.data;
      });
  }
};
</script>



<style >
@import '../assets/style.css';
</style>