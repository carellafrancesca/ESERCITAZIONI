package com.AbbonamentiPalestra.Repository;

import java.util.List;
import java.util.Optional;

import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

import com.AbbonamentiPalestra.Class.Abbonamenti;
import com.AbbonamentiPalestra.Class.TipoAbbonamento;
import com.AbbonamentiPalestra.Class.TipoAttivita;

@Repository
public interface AbbonamentiRepo extends CrudRepository<Abbonamenti, Long>{

	List<Abbonamenti> findByTipo(TipoAbbonamento tipo);

	List<Abbonamenti> findByAttivita(TipoAttivita attivita);
	
	List<Abbonamenti> findByAbbonatoNomeAndAbbonatoCognome(String nome, String cognome);

	// Per quanto riguarda il repository, i metodi findByTipo e findByAttivita devono essere implementati per filtrare gli abbonamenti in base al tipo e all'attività.
}
