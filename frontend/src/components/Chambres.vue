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
      
  <div>
    <header>
      <h1>Gestion des chambres</h1>
      <button class="btn" @click="ouvrirFormulaire()">+ Ajouter une chambre</button>
    </header>

    <section class="room-table">
      <h2>Liste des chambres</h2>
      <table>
        <thead>
          <tr>
            <th>Numéro</th>
            <th>Type</th>
            <th>Prix (Ar)</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="chambre in chambres" :key="chambre.id">
            <td>{{ chambre.numero }}</td>
            <td>{{ chambre.type }}</td>
            <td>{{ chambre.prix }}</td>
            <td class="actions">
              <button class="btn" @click="modifierChambre(chambre)">Modifier</button>
              <button class="btn btn-secondary" @click="supprimerChambre(chambre.id)">Supprimer</button>
            </td>
          </tr>
        </tbody>
      </table>
    </section>

    <section v-if="formVisible">
      <h2>{{ form.id ? 'Modifier' : 'Ajouter' }} une chambre</h2>
      <form @submit.prevent="soumettreChambre">
        <input v-model="form.numero" type="text" placeholder="Numéro" required />
        <input v-model="form.type" type="text" placeholder="Type" required />
        <input v-model="form.prix" type="number" placeholder="Prix" required />
        <button class="btn" type="submit">Enregistrer</button>
        <button class="btn btn-secondary" type="button" @click="annuler()">Annuler</button>
      </form>
    </section>
  </div>

    </main>
  </div>
</body>



</template>

<style>
@import '../assets/style.css';
</style>

<script>
export default {
  data() {
    return {
      chambres: [],
      form: {
        id: null,
        numero: '',
        type: '',
        prix: ''
      },
      formVisible: false
    }
  },
  created() {
    this.chargerChambres()
  },
  methods: {
    chargerChambres() {
      fetch("http://localhost:8000/api/chambres/")
        .then(res => res.json())
        .then(data => this.chambres = data)
        .catch(err => console.error("Erreur lors du chargement des chambres :", err));
    },
    ouvrirFormulaire() {
      this.form = { id: null, numero: '', type: '', prix: '' }
      this.formVisible = true
    },
    modifierChambre(chambre) {
      this.form = { ...chambre }
      this.formVisible = true
    },
    supprimerChambre(id) {
      fetch(`http://localhost:8000/api/chambres/${id}/`, {
        method: 'DELETE'
      })
      .then(() => this.chargerChambres())
      .catch(err => console.error("Erreur suppression :", err));
    },
    soumettreChambre() {
  // Convertir le prix en float avant l'envoi
  const chambrePayload = {
    ...this.form,
    prix: parseFloat(this.form.prix)
  };

  const url = this.form.id
    ? `http://localhost:8000/api/chambres/${this.form.id}/`
    : `http://localhost:8000/api/chambres/`;
  const method = this.form.id ? 'PUT' : 'POST';

  fetch(url, {
    method,
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(chambrePayload)
  })
    .then(() => {
      this.chargerChambres();
      this.formVisible = false;
    })
    .catch(err => console.error("Erreur enregistrement :", err));
}

,
    annuler() {
      this.formVisible = false
    }
  }
}
</script>
